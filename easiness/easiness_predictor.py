from collections import defaultdict
from random import Random

import numpy as np
from tqdm import tqdm

from structures.structure_extractor_ast import structuresExtractorAST
from structures.structure_extractor_surface import structuresExtractorSurfaceLevel
from utils.tokens_similarity import TokenSimilarityExtractor
from utils.lf_utils import tokenize_lf, TOKENS_TO_IGNORE
from utils.structure_utils import (
    get_structure_prefix_code,
    remove_prefixes,
    get_structures_per_prefix_dict,
)

USE_SURFACE_LEVEL_structures = False


class EasinessPredictor:
    """
    This class is initialized with the training examples of the dataset, so that later we can compute how easy a test
    example is by looking at the training dataset.
    """
    def __init__(self, train_examples, config):
        self._config = config
        self._random = Random()

        if self._config["structures"] is not False:
            # we support both looking at the AST of the program or surface-level (which is simply the sequence of symbols)
            if config["structures"]["type"] == "ast":
                self._structures_extractor = structuresExtractorAST(config["structures"])
            elif config["structures"]["type"] == "surface_level":
                self._structures_extractor = structuresExtractorSurfaceLevel(config["structures"])
            else:
                raise ValueError()

            # extract structures
            self._train_structures = self.get_structures(train_examples)
            
            # we have different prefixes for different types of structures - parent/child and siblings
            self._train_structures_per_prefix = get_structures_per_prefix_dict(
                self._train_structures
            )

            # pre-compute all similarities between different tokens - this is used for easiness computation
            self._similar_tokens = TokenSimilarityExtractor(
                self._train_structures
            ).find_all_similarities_between_tokens()

        # an alternative easiness prediction (not in paper), where tokens in unseen positions are predicted to be harder
        if self._config["position"] is not False:
            self._token_positions = self.get_token_positions(train_examples)

        # a simple baseline, where longer programs are harder
        if self._config["length"] is not False:
            self._max_length = self.get_max_length(train_examples)

    def get_structures(self, targets):
        all_structures = set()

        iterator = tqdm(targets) if len(targets) > 1 else targets

        for target in iterator:
            tokens = tokenize_lf(target, add_sos=True)
            try:
                ex_structures = self._structures_extractor.get_structures_from_target(tokens)
            except ValueError as e:
                print(f"Error parsing target: {target}")
                print(e)
                continue
            all_structures.update(ex_structures)

        return all_structures

    def predict_easiness_for_example(self, test_example):
        scores = []
        output = {}

        if self._config["structures"] is not False:
            structure_easiness = self.predict_structure_easiness_for_example(test_example)
            ex_structure_easiness = structure_easiness["predicted_easiness"]
            scores.append(ex_structure_easiness)
            output["structure"] = {
                "score": ex_structure_easiness,
                "debug_info": structure_easiness["debug"],
            }

        if self._config["position"] is not False:
            position_easiness = self.predict_token_position_easiness_for_example(
                test_example
            )
            ex_position_easiness = position_easiness["predicted_easiness"]
            scores.append(ex_position_easiness)
            output["position"] = {
                "score": ex_position_easiness,
                "debug_info": position_easiness["debug"],
            }

        if self._config["length"] is not False:
            ex_length_easiness = max(
                1 - len(tokenize_lf(test_example)) / self._max_length, 0
            )
            scores.append(ex_length_easiness)
            output["length"] = {"score": ex_length_easiness, "debug_info": {}}

        if self._config["random"] is not False:
            s = self._random.random()
            scores.append(s)
            output["random"] = {"score": s, "debug_info": {}}

        ex_agg_easiness = min(scores)
        output["final_score"] = ex_agg_easiness

        return output

    def predict_structure_easiness_for_example(self, test_example):
        cached_easiness = {}

        example_structures = self.get_structures([test_example])
        unseen_structures = example_structures.difference(self._train_structures)

        debug = {}

        example_easiness_scores = 1  # 1 is the max possible easiness currently
        for unseen_structure in unseen_structures:
            if unseen_structure not in cached_easiness:
                cached_easiness[unseen_structure] = self.predict_easiness_for_structure(
                    unseen_structure
                )
            structure_easiness_score, structure_debug_info = cached_easiness[unseen_structure]
            example_easiness_scores = min(structure_easiness_score, example_easiness_scores)
            debug[str(unseen_structure)] = structure_debug_info

        return {
            "predicted_easiness": example_easiness_scores,
            "unseen_structures": list(unseen_structures),
            "debug": debug,
        }

    def predict_easiness_for_structure(self, structure):
        n = len(structure)
        prefix_code = get_structure_prefix_code(structure)
        structure_no_prefix = remove_prefixes(structure)
        similar_to_token = {i: [] for i in range(n)}
        for i in range(n):
            if str(i) in self._config["find_similar"]:
                similar_to_token[i] = self._similar_tokens.get(structure_no_prefix[i])
            if not similar_to_token[i]:
                similar_to_token[i] = {structure_no_prefix[i]: 1}

        all_scores = []
        for i in range(n):
            for t, sim in similar_to_token[i].items():
                modified_structure = list(structure_no_prefix)
                modified_structure[i] = t
                modified_structure = tuple(modified_structure)
                if modified_structure in self._train_structures_per_prefix[prefix_code]:
                    all_scores.append((structure, modified_structure, sim))

        all_scores.sort(reverse=True, key=lambda x: x[2])

        if not all_scores:
            return 0, None
        else:
            top_score = all_scores[0]
            easiness = top_score[2]
            return easiness, top_score

    def predict_length_easiness_for_examples(
        self, split_train_max_length, test_examples
    ):
        all_examples_debug = {}
        all_predicted_easiness = []

        for example in test_examples:
            ex_length = len(tokenize_lf(example["target"], add_sos=False))
            ex_predicted_easiness = 1
            if ex_length > split_train_max_length:
                ex_predicted_easiness = max(
                    1 - (ex_length - split_train_max_length) / 10, 0
                )
            all_examples_debug[example["target"]] = ex_predicted_easiness
            all_predicted_easiness.append(ex_predicted_easiness)

        return {
            "predicted_easiness": all_predicted_easiness,
            "examples_debug": all_examples_debug,
        }

    def predict_token_position_easiness_for_example(self, test_example_target):
        ex_predicted_easiness = 1
        ex_hardest_token = ""
        for pos, token in enumerate(tokenize_lf(test_example_target, add_sos=False)):
            if token in TOKENS_TO_IGNORE:
                continue
            if token not in self._token_positions:
                # TODO: This shouldn't happen with valid splits!
                self._token_positions[token] = 50
            token_max_pos_in_train_mean = self._token_positions[token]

            if pos > token_max_pos_in_train_mean:
                token_predicted_easiness = max(
                    1 - (pos - token_max_pos_in_train_mean) / 10, 0
                )
                if token_predicted_easiness < ex_predicted_easiness:
                    ex_predicted_easiness = token_predicted_easiness
                    ex_hardest_token = token

        return {
            "predicted_easiness": ex_predicted_easiness,
            "debug": (ex_predicted_easiness, ex_hardest_token),
        }

    def get_token_positions(self, targets):
        positions = defaultdict(list)
        for target in targets:
            for p, token in enumerate(tokenize_lf(target, add_sos=False)):
                if token in TOKENS_TO_IGNORE:
                    continue
                positions[token].append(p)
        return {token: np.max(pos) for token, pos in positions.items()}

    @staticmethod
    def get_max_length(targets):
        lengths = []
        for target in targets:
            lengths.append(len(tokenize_lf(target, add_sos=False)))
        return np.max(lengths)

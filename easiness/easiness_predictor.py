from collections import defaultdict
from random import Random

import numpy as np
from tqdm import tqdm

from ngrams.ngram_extractor_ast import NgramsExtractorAST
from ngrams.ngram_extractor_surface import NgramsExtractorSurfaceLevel
from utils.tokens_similarity import TokenSimilarityExtractor
from utils.lf_utils import tokenize_lf, TOKENS_TO_IGNORE
from utils.ngram_utils import (
    get_ngram_prefix_code,
    remove_prefixes,
    get_ngrams_per_prefix_dict,
)

USE_SURFACE_LEVEL_NGRAMS = False


class EasinessPredictor:
    def __init__(self, train_examples, config):
        self._config = config
        self._random = Random()

        if self._config["ngrams"] is not False:
            if config["ngrams"]["type"] == "ast":
                self._ngrams_extractor = NgramsExtractorAST(config["ngrams"])
            elif config["ngrams"]["type"] == "surface_level":
                self._ngrams_extractor = NgramsExtractorSurfaceLevel(config["ngrams"])
            else:
                raise ValueError()

            self._train_ngrams = self.get_ngrams(train_examples)
            self._train_ngrams_per_prefix = get_ngrams_per_prefix_dict(
                self._train_ngrams
            )

            self._similar_tokens = TokenSimilarityExtractor(
                self._train_ngrams
            ).find_all_similarities_between_tokens()

        if self._config["position"] is not False:
            self._token_positions = self.get_token_positions(train_examples)

        if self._config["length"] is not False:
            self._max_length = self.get_max_length(train_examples)

    def get_ngrams(self, targets):
        all_ngrams = set()

        iterator = tqdm(targets) if len(targets) > 1 else targets

        for target in iterator:
            tokens = tokenize_lf(target, add_sos=True)
            try:
                ex_ngrams = self._ngrams_extractor.get_ngrams_from_target(tokens)
            except ValueError as e:
                print(f"Error parsing target: {target}")
                print(e)
                continue
            all_ngrams.update(ex_ngrams)

        return all_ngrams

    def predict_easiness_for_examples(self, test_example):
        scores = []
        output = {}

        if self._config["ngrams"] is not False:
            ngram_easiness = self.predict_ngram_easiness_for_example(test_example)
            ex_ngram_easiness = ngram_easiness["predicted_easiness"]
            scores.append(ex_ngram_easiness)
            output["ngram"] = {
                "score": ex_ngram_easiness,
                "debug_info": ngram_easiness["debug"],
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

    def predict_ngram_easiness_for_example(self, test_example):
        cached_easiness = {}

        example_ngrams = self.get_ngrams([test_example])
        unseen_ngrams = example_ngrams.difference(self._train_ngrams)

        debug = {}

        example_easiness_scores = 1  # 1 is the max possible easiness currently
        for unseen_ngram in unseen_ngrams:
            if unseen_ngram not in cached_easiness:
                cached_easiness[unseen_ngram] = self.predict_easiness_for_ngram(
                    unseen_ngram
                )
            ngram_easiness_score, ngram_debug_info = cached_easiness[unseen_ngram]
            example_easiness_scores = min(ngram_easiness_score, example_easiness_scores)
            debug[str(unseen_ngram)] = ngram_debug_info

        return {
            "predicted_easiness": example_easiness_scores,
            "unseen_ngrams": list(unseen_ngrams),
            "debug": debug,
        }

    def predict_easiness_for_ngram(self, ngram):
        n = len(ngram)
        prefix_code = get_ngram_prefix_code(ngram)
        ngram_no_prefix = remove_prefixes(ngram)
        similar_to_token = {i: [] for i in range(n)}
        for i in range(n):
            if str(i) in self._config["find_similar"]:
                similar_to_token[i] = self._similar_tokens.get(ngram_no_prefix[i])
            if not similar_to_token[i]:
                similar_to_token[i] = {ngram_no_prefix[i]: 1}

        all_scores = []
        for i in range(n):
            for t, sim in similar_to_token[i].items():
                modified_ngram = list(ngram_no_prefix)
                modified_ngram[i] = t
                modified_ngram = tuple(modified_ngram)
                if modified_ngram in self._train_ngrams_per_prefix[prefix_code]:
                    all_scores.append((ngram, modified_ngram, sim))

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

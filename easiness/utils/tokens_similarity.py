import numpy as np
from tqdm import tqdm

from utils.lf_utils import jaccard
from utils.structure_utils import get_structures_per_prefix_dict, remove_prefixes


class TokenSimilarityExtractor:
    def __init__(self, structures):
        self._unigrams = self._get_unigrams(structures)
        self._train_structures_per_prefix = get_structures_per_prefix_dict(structures)

    def find_all_similarities_between_tokens(self):
        self._find_all_tokens_contexts()

        similar_tokens = {}
        for token in tqdm(self._unigrams):
            similar_tokens[token] = self.get_similar_tokens(token)

        return similar_tokens

    def get_similar_tokens(self, token):
        token_context_per_prefix = self._token_context.get(token)

        if not token_context_per_prefix:
            return {token: 1}

        similarities = {}
        for other_token in self._unigrams:
            similarities_per_prefix = {}
            other_token_context_per_prefix = self._token_context[other_token]
            for prefix, other_token_contexts in other_token_context_per_prefix.items():
                similarities_per_direction = {}
                for (
                    direction,
                    other_token_context_in_direction,
                ) in other_token_contexts.items():
                    token_ctx = token_context_per_prefix[prefix][direction]
                    other_token_ctx = other_token_context_in_direction
                    if not token_ctx and not other_token_ctx:
                        continue
                    similarities_per_direction[direction] = jaccard(
                        token_ctx, other_token_ctx
                    )
                if similarities_per_direction:
                    similarities_per_prefix[prefix] = np.mean(
                        list(similarities_per_direction.values())
                    )
            if similarities_per_prefix:
                similarities[other_token] = np.mean(
                    list(similarities_per_prefix.values())
                )
            else:
                similarities[other_token] = 0

        similarities[token] = 1
        return similarities

    def _get_token_context_per_bigram_prefix(self, token):
        token_context_per_prefix = {}
        for prefix, structures in self._train_structures_per_prefix.items():
            # we only consider bigrams and not longer structures as context
            if len(prefix) != 2:
                continue

            token_context_per_prefix[prefix] = {}
            # these tokens appeared after `token` (either as a sibling or as a child, depending on the prefix code)
            token_context_per_prefix[prefix]["after"] = set(
                [b for (a, b) in structures if a == token]
            )
            # these tokens appeared before `token` (either as a sibling or as a child, depending on the prefix code)
            token_context_per_prefix[prefix]["before"] = set(
                [a for (a, b) in structures if b == token]
            )

        return token_context_per_prefix

    @staticmethod
    def _get_unigrams(structures):
        return {t for structure in structures for t in remove_prefixes(structure)}

    def _find_all_tokens_contexts(self):
        self._token_context = {}
        for token in tqdm(self._unigrams):
            self._token_context[token] = self._get_token_context_per_bigram_prefix(
                token
            )


def compute_structures_similarity(structure1, structure2, similarities):
    """
    Computes the similarity between *structures* based on similarity of their tokens
    """
    assert len(structure1) == len(structure1) > 0
    structure1_no_prefix, structure2_no_prefix = structure1, structure2
    for symb in structure1_no_prefix:
        if len(symb) > 2 and symb[1] == ":":
            structure1_no_prefix = remove_prefixes(structure1)
    for symb in structure2_no_prefix:
        if len(symb) > 2 and symb[1] == ":":
            structure2_no_prefix = remove_prefixes(structure2)

    n_diffs = 0
    sim = 1
    for symb1, symb2 in zip(structure1_no_prefix, structure2_no_prefix):
        if symb1 != symb2:
            n_diffs += 1

        if n_diffs > 1:
            return 0
        sim = min(sim, similarities[symb1][symb2])

    return sim


if __name__ == "__main__":
    similarities = {
        "a": {"a": 1, "b": 0.5, "c": 0.75, "d": 0.9},
        "b": {"a": 0.5, "b": 1, "c": 0.1, "d": 0.2},
        "c": {"a": 0.75, "b": 0.1, "c": 1, "d": 0.3},
        "d": {"a": 0.9, "b": 0.2, "c": 0.3, "d": 1},
    }
    assert compute_structures_similarity(("p:a", "c:b"), ("p:a", "c:b"), similarities) == 1
    assert compute_structures_similarity(("a", "b"), ("a", "b"), similarities) == 1
    assert compute_structures_similarity(("a", "b"), ("c", "d"), similarities) == 0
    assert compute_structures_similarity(("a", "b"), ("c", "d"), similarities) == 0
    assert compute_structures_similarity(("a", "b"), ("a", "d"), similarities) == 0.2
    assert compute_structures_similarity(("a", "b"), ("d", "b"), similarities) == 0.9
    assert (
        compute_structures_similarity(("a", "b", "c"), ("a", "a", "a"), similarities) == 0
    )
    assert (
        compute_structures_similarity(("a", "b", "c"), ("a", "d", "d"), similarities) == 0
    )
    assert (
        compute_structures_similarity(("a", "b", "c"), ("a", "b", "c"), similarities) == 1
    )
    assert (
        compute_structures_similarity(("a", "b", "c"), ("a", "b", "d"), similarities) == 0.3
    )
    assert (
        compute_structures_similarity(
            ("p:a", "s:b", "s:c"), ("p:a", "s:b", "s:d"), similarities
        )
        == 0.3
    )

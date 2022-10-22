from overrides import overrides

from structures.structure_extractor_base import structuresExtractor
from utils.lf_utils import TOKENS_TO_IGNORE


class structuresExtractorSurfaceLevel(structuresExtractor):
    def __init__(self, config):
        super().__init__(config)

    @overrides
    def _get_structures_from_target(self, target_tokens, freqs=False):
        tokens = [t for t in target_tokens if t not in TOKENS_TO_IGNORE]
        return set(tuple(tokens[i : i + 2]) for i in range(len(tokens) - 1))

from abc import abstractmethod


class structuresExtractor:
    _cached_structures_per_config = {}

    def __init__(self, config):
        self._config = config
        config_key = str(config)
        if config_key not in structuresExtractor._cached_structures_per_config:
            structuresExtractor._cached_structures_per_config[config_key] = {}

    def get_structures_from_target(self, target_tokens, freqs=False):
        config_key = str(self._config)
        cache_key = str(target_tokens)
        cached_structures = structuresExtractor._cached_structures_per_config.get(config_key).get(
            cache_key
        )
        if cached_structures:
            return cached_structures
        else:
            structuresExtractor._cached_structures_per_config[config_key][
                cache_key
            ] = self._get_structures_from_target(target_tokens, freqs=freqs)

        return structuresExtractor._cached_structures_per_config[config_key][cache_key]

    @abstractmethod
    def _get_structures_from_target(self, target, freqs=False):
        pass

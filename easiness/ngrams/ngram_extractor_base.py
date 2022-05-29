from abc import abstractmethod


class NgramsExtractor:
    _cached_ngrams_per_config = {}

    def __init__(self, config):
        self._config = config
        config_key = str(config)
        if config_key not in NgramsExtractor._cached_ngrams_per_config:
            NgramsExtractor._cached_ngrams_per_config[config_key] = {}

    def get_ngrams_from_target(self, target_tokens, freqs=False):
        config_key = str(self._config)
        cache_key = str(target_tokens)
        cached_ngrams = NgramsExtractor._cached_ngrams_per_config.get(config_key).get(
            cache_key
        )
        if cached_ngrams:
            return cached_ngrams
        else:
            NgramsExtractor._cached_ngrams_per_config[config_key][
                cache_key
            ] = self._get_ngrams_from_target(target_tokens, freqs=freqs)

        return NgramsExtractor._cached_ngrams_per_config[config_key][cache_key]

    @abstractmethod
    def _get_ngrams_from_target(self, target, freqs=False):
        pass

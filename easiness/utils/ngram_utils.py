from collections import defaultdict


def remove_prefixes(ngram):
    if ":" in ngram[0]:
        return tuple([t[2:] for t in ngram])
    else:
        return ngram


def get_ngram_prefix_code(ngram):
    return "".join([f"{t[0]}" for t in ngram])


def get_ngrams_per_prefix_dict(ngrams_with_prefixes):
    output = defaultdict(set)
    for ngram in ngrams_with_prefixes:
        prefix_code = get_ngram_prefix_code(ngram)
        output[prefix_code].add(remove_prefixes(ngram))
    return output

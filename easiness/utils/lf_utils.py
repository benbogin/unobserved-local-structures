TOKENS_TO_IGNORE = ["(", ")", ","]


def tokenize_lf(lf, add_sos=True):
    target = (
        lf.replace(" [ ", "[")
        .replace(" ]", "]")
        .replace("(", " ( ")
        .replace(")", " ) ")
        .replace(",", " , ")
    )
    if add_sos:
        target = f"<s> ( {target} )"
    tokens = target.split()
    return tokens


def jaccard(ngrams_with_same_first, ngrams_with_similar_token_as_first):
    inter = ngrams_with_same_first.intersection(ngrams_with_similar_token_as_first)
    uni = ngrams_with_same_first.union(ngrams_with_similar_token_as_first)
    return len(inter) / len(uni)

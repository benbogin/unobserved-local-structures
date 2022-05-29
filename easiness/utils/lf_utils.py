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


def jaccard(structures_with_same_first, structures_with_similar_token_as_first):
    inter = structures_with_same_first.intersection(structures_with_similar_token_as_first)
    uni = structures_with_same_first.union(structures_with_similar_token_as_first)
    return len(inter) / len(uni)

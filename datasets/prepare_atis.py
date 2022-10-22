import json

import re

from utils.ast_parser import ASTParser
from utils.lf_utils import tokenize_lf

f1 = open(r"atis-logic.txt")

ast_parser = ASTParser(config={})

f_out = open("atis/atis.all.jsonl", "wt")


def normalize_variables(t):
    """
    variables in atis dataset come in all kinds of shapes, so we normalize them here to make training easier and
    most importantly to make evaluation more accurate.
    """
    all_variables = re.findall('\$\w+', t)
    mapping = {}

    for v in all_variables:
        if v in mapping:
            continue
        mapping[v] = f"${len(mapping)}"

    new_t = t
    for v, n_v in mapping.items():
        new_t = new_t.replace(v, n_v)

    return new_t


for i, line in enumerate(f1):
    source, target = line.split('|||')
    source = source.strip()
    target = normalize_variables(target.strip())

    tokens = tokenize_lf(target, add_sos=False)

    anonymized_target = re.sub(r" ([^ ]*?) : (..)\b", r" value : \2", target)

    error_parsing = False
    try:
        ast_parser.get_ast(tokens)
    except ValueError:
        error_parsing = True
    if error_parsing:
        target += " )"
        tokens = tokenize_lf(target, add_sos=False)
        ast_parser.get_ast(tokens)

    f_out.write(json.dumps({
        'qid': f'atis_{i}',
        'source': source,
        'target': target,
        'anonymized': anonymized_target,
    }) + "\n")

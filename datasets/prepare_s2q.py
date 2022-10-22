import json

import re

from tqdm import tqdm

f1 = open(r"people.tsv")

f_out = open("s2q/s2q.all.jsonl", "wt")

seen_targets = set()

for i, line in enumerate(tqdm(f1)):
    line_values = line.strip().split('\t')
    source = line_values[2]
    non_anonymized_target = line_values[3]
    target = line_values[5]

    # remove redundant parts
    target = target.replace(" => notify", "")
    target = target.replace("now => ", "")

    # this specific string is not anonymized for some reason
    target = target.replace('"" p(q) ""', "QUOTED_VAL")

    # simplify fields such as param:knowsLanguage:Array
    target = re.sub(r'(\w*?):([\w|\.]*?):(.*? )', r'\2 ', target)

    # simplify entities org.schema.Person:Organization
    target = re.sub(r'(org\.schema\.)(\w*?):(\w*?)([\)| ])', r'\3\4', target)
    target = re.sub(r'(@org\.schema\.)(\w*?).(\w*?)([\)| ])', r'\3\4', target)

    # replacing the entity with filter makes more sense parsing-wise
    target = target.replace("( Person ) filter", "filter ( Person )")

    # remove types
    target = re.sub(r'\^\^([\w|\.|:]*)(?= |$)', ' ', target)

    # add filter condition parentheses
    target = re.sub(r'(filter \( Person \))(.*?)(VAL(?! [,|\]])|VAL \])', r'\1 ( \2\3 )', target)
    target = re.sub(r'( or | and )(.*?)(VAL(?! [,|\]])|VAL \])', r'\1 ( \2\3 )', target)

    # add a select function when program starts with square brackets (our parser expects parentheses-based functions)
    target = re.sub(r'^\[(.*?)\]', r'fields (\1)', target)
    target = re.sub(r'^\[(.*?)\]', r'fields (\1)', target)

    assert (line_values[5].count("and") == target.count("and"))
    assert "[ QUOTED_VAL )" not in target
    assert "QUOTED_ VAL" not in target

    # some weird cases
    if '"' in target or "^^" in target:
        continue

    target = ' '.join(target.split())

    # anonymize source
    found_values = list(re.finditer('"" (.*?) ""', non_anonymized_target))
    for value_match in found_values:
        # we want to find the column aligned with this value, so we look to the left of the value
        pos = value_match.regs[1]
        value = non_anonymized_target[pos[0]:pos[1]]
        left_of_value = non_anonymized_target[:pos[0]]
        aligned_param = re.findall("param:([^:]*)", left_of_value)[-1]
        source = source.replace(value, f'"{aligned_param}"')

    if target not in seen_targets:
        seen_targets.add(target)
        print(target)

    f_out.write(json.dumps({
        'qid': f's2q_people_{i}',
        'source': source,
        'target': target,
    }) + "\n")

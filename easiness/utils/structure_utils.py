from collections import defaultdict


def remove_prefixes(structure):
    if ":" in structure[0]:
        return tuple([t[2:] for t in structure])
    else:
        return structure


def get_structure_prefix_code(structure):
    return "".join([f"{t[0]}" for t in structure])


def get_structures_per_prefix_dict(structures_with_prefixes):
    output = defaultdict(set)
    for structure in structures_with_prefixes:
        prefix_code = get_structure_prefix_code(structure)
        output[prefix_code].add(remove_prefixes(structure))
    return output

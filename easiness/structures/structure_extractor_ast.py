from overrides import overrides
from collections import Counter

from utils.ast_parser import ASTParser
from structures.structure_extractor_base import structuresExtractor


class structuresExtractorAST(structuresExtractor):
    def __init__(self, config):
        super().__init__(config)

        self._ast_parser = ASTParser(config={})

    @overrides
    def _get_structures_from_target(self, target_tokens, freqs=False):
        parsed_target = self._ast_parser.get_ast(target_tokens)
        return self._get_structures_from_ast_rec(parsed_target, freqs=freqs)

    def _get_structures_from_ast_rec(self, ast, ancestors=None, siblings=None, freqs=False):
        output = Counter() if freqs else set()
        if not ast:
            return output

        ancestors = ancestors or []
        siblings = siblings or []

        def representative_string(elements):
            if type(elements) is str or type(elements) is int:
                return str(elements)
            elif type(elements) is list:
                if len(elements):
                    return representative_string(elements[0])
                else:
                    return ""
            assert False

        reps = [representative_string(elm) for elm in ast]

        if not freqs:
            # we need to take care of a special case where ast[0] is lambda function: a list with 'lambda' as first token.
            # in such cases we will want to recurse on that list too
            if type(ast[0]) is list:
                output.update(
                    self._get_structures_from_ast_rec(ast[0], ancestors, siblings)
                )

            max_siblings = (
                min(self._config["n"] - 1, len(siblings))
                if self._config["add_adjacent_sibling"]
                else 0
            )
            max_parents = (
                min(self._config["n"] - 1, len(ancestors))
                if self._config["add_parent_child"]
                else 0
            )
            # go through each combination of n_parents and n_siblings to create our tuples
            for n_siblings_to_add in range(max_siblings + 1):
                for n_parents_to_add in range(max_parents + 1):
                    if (
                        n_parents_to_add + n_siblings_to_add == 0
                        or n_parents_to_add + n_siblings_to_add + 1 > self._config["n"]
                    ):
                        continue
                    structures_tuple = []
                    for i in range(n_parents_to_add, 0, -1):
                        structures_tuple.append(f"p:" + ancestors[-i])
                    for i in range(n_siblings_to_add, 0, -1):
                        structures_tuple.append("s:" + siblings[-i])
                    structures_tuple.append("c:" + reps[0])
                    output.add(tuple(structures_tuple))

            ancestors.append(reps[0])

            for i, (rep, elm) in enumerate(zip(reps, ast)):
                if i == 0:
                    continue
                if type(elm) is list:
                    output.update(
                        self._get_structures_from_ast_rec(elm, ancestors, reps[1:i])
                    )
                elif type(elm) is str:
                    output.update(
                        self._get_structures_from_ast_rec([elm], ancestors, reps[1:i])
                    )
            ancestors.pop()
        else:
            # we need to take care of a special case where ast[0] is lambda function: a list with 'lambda' as first token.
            # in such cases we will want to recurse on that list too
            if type(ast[0]) is list:
                output.update(
                    self._get_structures_from_ast_rec(
                        ast[0], ancestors, siblings, freqs=freqs
                    )
                )

            max_siblings = (
                min(self._config["n"] - 1, len(siblings))
                if self._config["add_adjacent_sibling"]
                else 0
            )
            max_parents = (
                min(self._config["n"] - 1, len(ancestors))
                if self._config["add_parent_child"]
                else 0
            )
            # go through each combination of n_parents and n_siblings to create our tuples
            for n_siblings_to_add in range(max_siblings + 1):
                for n_parents_to_add in range(max_parents + 1):
                    if (
                        n_parents_to_add + n_siblings_to_add == 0
                        or n_parents_to_add + n_siblings_to_add + 1 > self._config["n"]
                    ):
                        continue
                    structures_tuple = []
                    for i in range(n_parents_to_add, 0, -1):
                        structures_tuple.append(f"p:" + ancestors[-i])
                    for i in range(n_siblings_to_add, 0, -1):
                        structures_tuple.append("s:" + siblings[-i])
                    structures_tuple.append("c:" + reps[0])
                    output[tuple(structures_tuple)] += 1

            ancestors.append(reps[0])

            for i, (rep, elm) in enumerate(zip(reps, ast)):
                if i == 0:
                    continue
                if type(elm) is list:
                    output.update(
                        self._get_structures_from_ast_rec(
                            elm, ancestors, reps[1:i], freqs=freqs
                        )
                    )
                elif type(elm) is str:
                    output.update(
                        self._get_structures_from_ast_rec(
                            [elm], ancestors, reps[1:i], freqs=freqs
                        )
                    )
            ancestors.pop()
        return output

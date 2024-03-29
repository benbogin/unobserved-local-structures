from typing import List, Any


class ASTParser:
    _cached_ast_per_config = {}

    def __init__(self, config):
        self._config = config
        config_key = str(config)
        if config_key not in ASTParser._cached_ast_per_config:
            ASTParser._cached_ast_per_config[config_key] = {}

    def get_ast(self, input_norm: List[str]) -> List[Any]:
        config_key = str(self._config)
        cache_key = str(input_norm)
        if cache_key in ASTParser._cached_ast_per_config.get(config_key):
            return ASTParser._cached_ast_per_config[config_key][cache_key]

        ast = self._get_ast_rec(input_norm)
        ASTParser._cached_ast_per_config[config_key][cache_key] = ast

        return ast

    def _get_ast_rec(self, input_norm: List[str]) -> List[Any]:
        ast = []

        input_norm = [
            token for token in input_norm if token not in ["call", "string", "number"]
        ]

        elements = []
        current_element = []
        i = 0
        while i < len(input_norm):
            symbol = input_norm[i]
            if symbol == "(":
                list_content = []
                match_ctr = 1  # If 0, parenthesis has been matched.
                while match_ctr != 0:
                    i += 1
                    if i >= len(input_norm):
                        raise ValueError("Invalid input: Unmatched open parenthesis.")
                    symbol = input_norm[i]
                    if symbol == "(":
                        match_ctr += 1
                    elif symbol == ")":
                        match_ctr -= 1
                    if match_ctr != 0:
                        list_content.append(symbol)
                current_element += self._get_ast_rec(list_content)
            elif symbol == ")":
                raise ValueError("Invalid input: Unmatched close parenthesis.")
            elif symbol == ",":
                elements.append(current_element)
                current_element = []
            else:
                current_element.append(symbol)
            i += 1
        elements.append(current_element)
        ast += elements

        return ast

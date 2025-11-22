from typing import List, Union, Dict

class Solution:
    def evaluate(self, expression: str) -> int:

        def get_tokens(expression: str) -> List[Union[str, List]]:
            tokens = []
            buf = ''
            depth = 0
            for char in expression:
                if char == ' ' and depth == 0:
                    if buf:
                        tokens.append(buf)
                        buf = ''
                else:
                    if char == '(':
                        depth += 1
                    elif char == ')':
                        depth -= 1
                    buf += char
            if buf:
                tokens.append(buf)
            return tokens

        def evaluate_expression(tokens: Union[List, str], context: Dict[str, int]) -> int:
            if isinstance(tokens, str):
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]

            if tokens[0] == 'add':
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            elif tokens[0] == 'mult':
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            elif tokens[0] == 'let':
                new_context = dict(context)
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    val = evaluate_expression(expr, new_context)
                    new_context[var] = val
                    i += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                # Should not be reached if input is valid, but fallback
                try:
                    return int(tokens[0])
                except:
                    return context[tokens[0]]

        def parse_expression(expression: str) -> Union[List, str]:
            if not expression or expression[0] != '(':
                return expression
            inner = expression[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
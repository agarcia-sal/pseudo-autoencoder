from typing import List, Union, Dict


class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> List[str]:
            tokens = []
            buf = []
            depth = 0
            for char in expression:
                if char == ' ' and depth == 0:
                    if buf:
                        tokens.append(''.join(buf))
                        buf = []
                else:
                    if char == '(':
                        depth += 1
                    elif char == ')':
                        depth -= 1
                    buf.append(char)
            if buf:
                tokens.append(''.join(buf))
            return tokens

        def parse_expression(expression: str) -> Union[str, List]:
            if not expression or expression[0] != '(':
                return expression
            inner = expression[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens: Union[str, List], context: Dict[str, int]) -> int:
            if isinstance(tokens, str):
                # tokens is a single token, could be variable name or int literal
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]
            op = tokens[0]
            if op == 'add':
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            elif op == 'mult':
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            elif op == 'let':
                new_context = context.copy()
                i = 1
                # last token is the expression to return
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    new_context[var] = evaluate_expression(expr, new_context)
                    i += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                # Should not reach here in well-formed expressions
                raise ValueError(f"Unknown operation or token: {op}")

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
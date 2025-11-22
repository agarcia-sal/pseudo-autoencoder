from typing import List, Union, Dict

class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expr: str) -> List[str]:
            tokens = []
            buf = ''
            depth = 0
            for ch in expr:
                if ch == ' ' and depth == 0:
                    if buf:
                        tokens.append(buf)
                        buf = ''
                else:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    buf += ch
            if buf:
                tokens.append(buf)
            return tokens

        def parse_expression(expr: str) -> Union[str, List]:
            if not expr or expr[0] != '(':
                return expr
            inner = expr[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens: Union[str, List], context: Dict[str, int]) -> int:
            if isinstance(tokens, str):
                # Try integer conversion first, else lookup in context
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]

            op = tokens[0]
            if op == 'add':
                # tokens: ['add', expr1, expr2]
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            elif op == 'mult':
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            elif op == 'let':
                new_context = context.copy()
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    val = evaluate_expression(expr, new_context)
                    new_context[var] = val
                    i += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                # Should not reach here if input valid, fallback to int or context lookup
                try:
                    return int(op)
                except ValueError:
                    return context[op]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
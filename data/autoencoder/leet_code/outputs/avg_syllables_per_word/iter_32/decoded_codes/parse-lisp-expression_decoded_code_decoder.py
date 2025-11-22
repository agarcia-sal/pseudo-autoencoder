from copy import deepcopy

class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> list[str]:
            tokens = []
            buf = []
            depth = 0
            for ch in expression:
                if ch == ' ' and depth == 0:
                    if buf:
                        tokens.append(''.join(buf))
                        buf = []
                else:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    buf.append(ch)
            if buf:
                tokens.append(''.join(buf))
            return tokens

        def evaluate_expression(tokens, context):
            # tokens is either str or list
            if isinstance(tokens, str):
                # Try int conversion
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]

            if not tokens:
                raise ValueError("Empty expression encountered")

            op = tokens[0]

            if op == 'add':
                # tokens[1], tokens[2] are expressions
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            elif op == 'mult':
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            elif op == 'let':
                new_context = deepcopy(context)
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    val = evaluate_expression(expr, new_context)
                    new_context[var] = val
                    i += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                # Single variable or integer string
                # Defensive fallback:
                try:
                    return int(op)
                except ValueError:
                    return context[op]

        def parse_expression(expression: str):
            expression = expression.strip()
            if not expression:
                raise ValueError("Empty expression string")

            if expression[0] != '(':
                return expression

            # Remove outer parentheses
            inner_expression = expression[1:-1].strip()
            tokens = get_tokens(inner_expression)
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
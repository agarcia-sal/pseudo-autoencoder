class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> list[str]:
            tokens = []
            buf = ""
            depth = 0
            for ch in expression:
                if ch == ' ' and depth == 0:
                    if buf:
                        tokens.append(buf)
                        buf = ""
                else:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    buf += ch
            if buf:
                tokens.append(buf)
            return tokens

        def parse_expression(expression: str | list) -> list | str:
            if isinstance(expression, str) and (len(expression) == 0 or expression[0] != '('):
                return expression
            if isinstance(expression, str):
                inner = expression[1:-1]
                tokens = get_tokens(inner)
                return [parse_expression(token) for token in tokens]
            return expression  # already parsed list

        def evaluate_expression(tokens: list | str, context: dict) -> int:
            if isinstance(tokens, str):
                # token is single string: try int else variable lookup
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]
            # tokens is list
            op = tokens[0]
            if op == "add":
                # tokens[1], tokens[2]
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            elif op == "mult":
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            elif op == "let":
                new_context = context.copy()
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    new_context[var] = evaluate_expression(expr, new_context)
                    i += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                # Not expected to reach here with valid input, fallback
                try:
                    return int(op)
                except ValueError:
                    return context[op]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
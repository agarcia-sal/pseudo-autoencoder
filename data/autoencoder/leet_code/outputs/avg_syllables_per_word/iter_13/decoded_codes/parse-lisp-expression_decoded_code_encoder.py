class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> list[str]:
            tokens = []
            buf = ''
            depth = 0
            for ch in expression:
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

        def evaluate_expression(tokens, context: dict) -> int:
            if isinstance(tokens, list):
                # tokens is a list starting with operator or 'let'
                if tokens[0] == 'add':
                    return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
                elif tokens[0] == 'mult':
                    return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
                elif tokens[0] == 'let':
                    new_context = context.copy()
                    i = 1
                    while i < len(tokens) - 1:
                        var = tokens[i]
                        expr = tokens[i + 1]
                        new_context[var] = evaluate_expression(expr, new_context)
                        i += 2
                    return evaluate_expression(tokens[-1], new_context)
                else:
                    # If first token is neither of above, treat as variable/expression
                    # Defensive fallback: try to resolve as int or from context
                    try:
                        return int(tokens[0])
                    except (ValueError, TypeError):
                        return context[tokens[0]]
            else:
                # tokens is a string - could be number or variable
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]

        def parse_expression(expression: str):
            if not expression or expression[0] != '(':
                return expression
            inner = expression[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
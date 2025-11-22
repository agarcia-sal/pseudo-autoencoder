class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> list[str]:
            tokens = []
            buf = ''
            depth = 0
            for char in expression:
                if char == ' ' and depth == 0:
                    if buf != '':
                        tokens.append(buf)
                        buf = ''
                else:
                    if char == '(':
                        depth += 1
                    elif char == ')':
                        depth -= 1
                    buf += char
            if buf != '':
                tokens.append(buf)
            return tokens

        def evaluate_expression(tokens, context):
            if isinstance(tokens, list):
                if not tokens:
                    raise ValueError("Empty token list")
                op = tokens[0]
                if op == 'add':
                    # Expect exactly three tokens: add, expr1, expr2
                    return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
                elif op == 'mult':
                    # Expect exactly three tokens: mult, expr1, expr2
                    return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
                elif op == 'let':
                    new_context = context.copy()
                    i = 1
                    # Tokens between 1 and len(tokens)-2 represent variable assignments in pairs
                    # The last token is the expr to evaluate
                    while i < len(tokens) - 1:
                        var = tokens[i]
                        expr = tokens[i + 1]
                        val = evaluate_expression(expr, new_context)
                        new_context[var] = val
                        i += 2
                    return evaluate_expression(tokens[-1], new_context)
                else:
                    # This should not happen normally
                    # but just in case, treat op as variable or int
                    try:
                        return int(op)
                    except ValueError:
                        return context[op]
            else:
                # tokens is a string (not list)
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]

        def parse_expression(expression: str):
            expression = expression.strip()
            if not expression or expression[0] != '(':
                return expression
            # Remove outer parentheses
            inner = expression[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str):
            tokens = []
            buffer = ''
            depth = 0
            for char in expression:
                if char == ' ' and depth == 0:
                    if buffer:
                        tokens.append(buffer)
                        buffer = ''
                else:
                    if char == '(':
                        depth += 1
                    elif char == ')':
                        depth -= 1
                    buffer += char
            if buffer:
                tokens.append(buffer)
            return tokens

        def evaluate_expression(tokens, context):
            if isinstance(tokens, list):
                if not tokens:
                    # Defensive: empty list, invalid, return 0
                    return 0
                op = tokens[0]
                if op == 'add':
                    return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
                elif op == 'mult':
                    return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
                elif op == 'let':
                    new_context = context.copy()
                    i = 1
                    while i < len(tokens) - 1:
                        var = tokens[i]
                        expr = tokens[i + 1]
                        new_context[var] = evaluate_expression(expr, new_context)
                        i += 2
                    return evaluate_expression(tokens[-1], new_context)
                else:
                    # Unexpected operation token, try to evaluate as int or variable
                    try:
                        return int(op)
                    except ValueError:
                        return context[op]
            else:
                # tokens is a string
                if tokens.startswith('('):
                    # Should not get here because parse_expression returns list for parenthesis
                    # But just in case, parse again
                    parsed = parse_expression(tokens)
                    return evaluate_expression(parsed, context)
                else:
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
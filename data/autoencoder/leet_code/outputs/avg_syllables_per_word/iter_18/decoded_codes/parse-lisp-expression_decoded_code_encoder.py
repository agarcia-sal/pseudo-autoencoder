class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> list[str]:
            tokens = []
            buffer = ""
            depth = 0
            for ch in expression:
                if ch == ' ' and depth == 0:
                    if buffer:
                        tokens.append(buffer)
                        buffer = ""
                else:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    buffer += ch
            if buffer:
                tokens.append(buffer)
            return tokens

        def evaluate_expression(tokens, context):
            if isinstance(tokens, list):
                op = tokens[0]
                if op == 'add':
                    return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
                elif op == 'mult':
                    return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
                elif op == 'let':
                    new_context = context.copy()
                    index = 1
                    while index < len(tokens) - 1:
                        var = tokens[index]
                        expr = tokens[index + 1]
                        val = evaluate_expression(expr, new_context)
                        new_context[var] = val
                        index += 2
                    return evaluate_expression(tokens[-1], new_context)
                else:
                    # Unexpected operation, treat as variable or int fallback
                    try:
                        return int(op)
                    except:
                        return context[op]
            else:
                # tokens is a string: either integer literal or variable name
                try:
                    return int(tokens)
                except:
                    return context[tokens]

        def parse_expression(expression: str):
            if not expression.startswith('('):
                return expression
            inner_expression = expression[1:-1]
            tokens = get_tokens(inner_expression)
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
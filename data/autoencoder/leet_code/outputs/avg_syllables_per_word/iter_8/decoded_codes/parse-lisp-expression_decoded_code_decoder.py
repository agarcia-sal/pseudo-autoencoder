class Solution:
    def evaluate(self, expression):
        def get_tokens(expression):
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
            if isinstance(tokens, list) and len(tokens) > 0:
                if tokens[0] == 'add':
                    return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
                elif tokens[0] == 'mult':
                    return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
                elif tokens[0] == 'let':
                    new_context = context.copy()
                    i = 1
                    while i < len(tokens) - 1:
                        var = tokens[i]
                        expr = tokens[i+1]
                        new_context[var] = evaluate_expression(expr, new_context)
                        i += 2
                    return evaluate_expression(tokens[-1], new_context)
            # If not an expression list or no recognized operation -> literal or variable
            try:
                return int(tokens)
            except (ValueError, TypeError):
                return context[tokens]

        def parse_expression(expression):
            if not expression.startswith('('):
                return expression
            tokens = get_tokens(expression[1:-1])
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
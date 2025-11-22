class Solution:
    def evaluate(self, expression):
        def get_tokens(expression):
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

        def parse_expression(expression):
            if not expression or expression[0] != '(':
                return expression
            tokens = get_tokens(expression[1:-1])
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens, context):
            if isinstance(tokens, str):
                # tokens is a variable or a literal integer
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]
            if not tokens:
                return 0  # handle empty tokens safely

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
                # Should not reach here if input is valid
                try:
                    return int(op)
                except ValueError:
                    return context[op]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
from copy import deepcopy

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

        def evaluate_expression(tokens, context):
            if isinstance(tokens, list) and tokens:
                op = tokens[0]
                if op == 'add':
                    return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
                elif op == 'mult':
                    return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
                elif op == 'let':
                    new_context = deepcopy(context)
                    i = 1
                    while i < len(tokens) - 1:
                        var = tokens[i]
                        expr = tokens[i+1]
                        new_context[var] = evaluate_expression(expr, new_context)
                        i += 2
                    return evaluate_expression(tokens[-1], new_context)
                else:
                    # It should not reach here as op must be add/mult/let or a value
                    pass

            # tokens here is not a list, so evaluate it as int or var
            token = tokens
            try:
                return int(token)
            except ValueError:
                return context[token]

        def parse_expression(expression):
            if not expression or expression[0] != '(':
                return expression
            inner = expression[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expr: str) -> list:
            tokens, buf, depth = [], '', 0
            for char in expr:
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

        def parse_expression(expr: str):
            if not expr or expr[0] != '(':
                return expr
            inner = expr[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(t) for t in tokens]

        def evaluate_expression(tokens, context):
            if isinstance(tokens, str):
                try:
                    return int(tokens)
                except:
                    return context[tokens]
            op = tokens[0]
            if op == 'add':
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            if op == 'mult':
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            if op == 'let':
                new_context = context.copy()
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    new_context[var] = evaluate_expression(expr, new_context)
                    i += 2
                return evaluate_expression(tokens[-1], new_context)

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
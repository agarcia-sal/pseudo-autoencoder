from copy import deepcopy

class Solution:
    def evaluate(self, expression):
        def get_tokens(expression):
            tokens = []
            buf = []
            depth = 0
            for ch in expression:
                if ch == ' ' and depth == 0:
                    if buf:
                        tokens.append(''.join(buf))
                        buf.clear()
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
            head = tokens[0]
            if head == "add":
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            elif head == "mult":
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            elif head == "let":
                new_context = deepcopy(context)
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    new_context[var] = evaluate_expression(expr, new_context)
                    i += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                try:
                    return int(head)
                except ValueError:
                    return context[head]

        def parse_expression(expression):
            if not expression or expression[0] != '(':
                return expression
            inner = expression[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(tok) for tok in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
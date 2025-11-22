from copy import deepcopy

class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expr: str) -> list[str]:
            tokens = []
            buffer = []
            depth = 0
            for ch in expr:
                if ch == ' ' and depth == 0:
                    if buffer:
                        tokens.append(''.join(buffer))
                        buffer = []
                else:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    buffer.append(ch)
            if buffer:
                tokens.append(''.join(buffer))
            return tokens

        def parse_expression(expr: str):
            if not expr or expr[0] != '(':
                return expr
            inner = expr[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens, context):
            if isinstance(tokens, str):
                # Could be a number or a variable reference
                try:
                    return int(tokens)
                except ValueError:
                    if tokens in context:
                        return context[tokens]
                    else:
                        raise ValueError(f"Undefined variable: {tokens}")

            # tokens is a list, tokens[0] is operator: "add", "mult", "let"
            operator = tokens[0]
            if operator == "add":
                # add <expr1> <expr2>
                return evaluate_expression(tokens[1], context) + evaluate_expression(tokens[2], context)
            elif operator == "mult":
                # mult <expr1> <expr2>
                return evaluate_expression(tokens[1], context) * evaluate_expression(tokens[2], context)
            elif operator == "let":
                # let var1 expr1 var2 expr2 ... exprN
                new_context = deepcopy(context)
                i = 1
                # The last token is the expr to return
                while i < len(tokens) - 1:
                    variable = tokens[i]
                    expr = tokens[i + 1]
                    val = evaluate_expression(expr, new_context)
                    new_context[variable] = val
                    i += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                # If not recognized operator, try to interpret as int or variable
                try:
                    return int(tokens)
                except ValueError:
                    if tokens in context:
                        return context[tokens]
                    else:
                        raise ValueError(f"Unknown operator or undefined variable: {tokens}")

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> list[str]:
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

        def parse_expression(expression: str | list) -> str | list:
            if not isinstance(expression, str):
                return expression
            if not expression or expression[0] != '(':
                return expression
            tokens = get_tokens(expression[1:-1])
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens: str | list, context: dict[str, int]) -> int:
            if isinstance(tokens, str):
                try:
                    return int(tokens)
                except ValueError:
                    return context[tokens]
            if not tokens:
                raise ValueError("Empty token list")
            op = tokens[0]
            if op == 'add':
                val1 = evaluate_expression(tokens[1], context)
                val2 = evaluate_expression(tokens[2], context)
                return val1 + val2
            elif op == 'mult':
                val1 = evaluate_expression(tokens[1], context)
                val2 = evaluate_expression(tokens[2], context)
                return val1 * val2
            elif op == 'let':
                new_context = context.copy()
                idx = 1
                while idx < len(tokens) - 1:
                    var = tokens[idx]
                    expr = tokens[idx + 1]
                    val = evaluate_expression(expr, new_context)
                    new_context[var] = val
                    idx += 2
                return evaluate_expression(tokens[-1], new_context)
            else:
                # This covers variables or integer values directly
                try:
                    return int(tokens[0])
                except ValueError:
                    return context[tokens[0]]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
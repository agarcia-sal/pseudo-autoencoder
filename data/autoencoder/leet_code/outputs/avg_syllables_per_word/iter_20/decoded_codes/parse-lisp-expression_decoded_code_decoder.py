class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expr: str) -> list[str]:
            tokens = []
            buf = []
            depth = 0
            i = 0
            length = len(expr)
            while i < length:
                c = expr[i]
                if c == ' ' and depth == 0:
                    if buf:
                        tokens.append(''.join(buf))
                        buf.clear()
                else:
                    if c == '(':
                        depth += 1
                    elif c == ')':
                        depth -= 1
                    buf.append(c)
                i += 1
            if buf:
                tokens.append(''.join(buf))
            return tokens

        def parse_expression(expr: str):
            if not expr:
                return expr
            expr = expr.strip()
            if not expr.startswith('('):
                return expr
            # Remove outer parentheses and parse tokens inside
            inner = expr[1:-1].strip()
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens, context: dict) -> int:
            if isinstance(tokens, str):
                # Token is a single symbol or integer literal
                try:
                    return int(tokens)
                except ValueError:
                    if tokens in context:
                        return context[tokens]
                    else:
                        raise ValueError(f"Undefined variable: {tokens}")
            # tokens is a list: [operator, ...args]
            if not tokens:
                raise ValueError("Empty expression")
            op = tokens[0]
            if op == 'add':
                if len(tokens) != 3:
                    raise ValueError("add expects exactly two arguments")
                left = evaluate_expression(tokens[1], context)
                right = evaluate_expression(tokens[2], context)
                return left + right
            elif op == 'mult':
                if len(tokens) != 3:
                    raise ValueError("mult expects exactly two arguments")
                left = evaluate_expression(tokens[1], context)
                right = evaluate_expression(tokens[2], context)
                return left * right
            elif op == 'let':
                if len(tokens) < 3:
                    raise ValueError("let expects at least two arguments")
                new_context = context.copy()
                i = 1
                # Process var-expr pairs except the last token which is the expression to evaluate
                # The pairs end at len(tokens)-1 - 1 if len(tokens) is odd
                # But safer to process pairs until the last token
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    if not isinstance(var, str):
                        raise ValueError("Variable name in let must be string")
                    val = evaluate_expression(expr, new_context)
                    new_context[var] = val
                    i += 2
                # Last token is expression to evaluate with updated context
                return evaluate_expression(tokens[-1], new_context)
            else:
                # Fallback: tokens[0] might be a number or variable
                try:
                    return int(op)
                except ValueError:
                    if op in context:
                        return context[op]
                    else:
                        raise ValueError(f"Unknown operator or variable: {op}")

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
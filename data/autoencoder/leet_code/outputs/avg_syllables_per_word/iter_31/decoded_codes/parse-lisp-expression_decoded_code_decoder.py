from typing import List, Union, Dict


class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression: str) -> List[str]:
            tokens = []
            buf = []
            depth = 0
            for c in expression:
                if c == ' ' and depth == 0:
                    if buf:
                        tokens.append(''.join(buf))
                        buf = []
                else:
                    if c == '(':
                        depth += 1
                    elif c == ')':
                        depth -= 1
                    buf.append(c)
            if buf:
                tokens.append(''.join(buf))
            return tokens

        def parse_expression(expression: str) -> Union[str, List]:
            if not expression:
                return ""
            if expression[0] != '(':
                return expression
            inner = expression[1:-1]
            tokens = get_tokens(inner)
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens: Union[str, List], context: Dict[str, int]) -> int:
            if isinstance(tokens, str):
                # tokens is a single token that is either an int or variable
                try:
                    return int(tokens)
                except ValueError:
                    if tokens not in context:
                        raise ValueError(f"Undefined variable: {tokens}")
                    return context[tokens]

            # tokens is a list, commands are always non-empty
            if not tokens:
                raise ValueError("Empty expression")

            operator = tokens[0]
            if operator == 'add':
                if len(tokens) != 3:
                    raise ValueError(f"'add' expects exactly 2 arguments, got {len(tokens)-1}")
                left = evaluate_expression(tokens[1], context)
                right = evaluate_expression(tokens[2], context)
                return left + right

            elif operator == 'mult':
                if len(tokens) != 3:
                    raise ValueError(f"'mult' expects exactly 2 arguments, got {len(tokens)-1}")
                left = evaluate_expression(tokens[1], context)
                right = evaluate_expression(tokens[2], context)
                return left * right

            elif operator == 'let':
                # let can have more than 2 tokens
                if len(tokens) < 2:
                    raise ValueError("'let' expects at least 1 argument")

                new_context = context.copy()
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    expr = tokens[i + 1]
                    if not isinstance(var, str):
                        raise ValueError(f"Invalid variable name in let: {var}")
                    value = evaluate_expression(expr, new_context)
                    new_context[var] = value
                    i += 2
                # last token is expression to evaluate in new_context
                return evaluate_expression(tokens[-1], new_context)

            else:
                # means tokens[0] is a token to resolve (should not happen here as operator always one of add/mult/let)
                # fallback parsing single token
                return evaluate_expression(operator, context)

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
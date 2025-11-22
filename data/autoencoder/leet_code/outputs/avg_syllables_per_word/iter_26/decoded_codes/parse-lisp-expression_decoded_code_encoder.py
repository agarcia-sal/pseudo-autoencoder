class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression_string: str) -> list[str]:
            tokens = []
            buf = ""
            depth = 0
            for ch in expression_string:
                if ch == ' ' and depth == 0:
                    tokens.append(buf)
                    buf = ""
                else:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    buf += ch
            if buf:
                tokens.append(buf)
            return tokens

        def evaluate_expression(tokens_list, context_dictionary):
            if isinstance(tokens_list, str):
                # Base case: token is either a variable or an int literal
                try:
                    return int(tokens_list)
                except ValueError:
                    return context_dictionary[tokens_list]

            if tokens_list[0] == 'add':
                return evaluate_expression(tokens_list[1], context_dictionary) + evaluate_expression(tokens_list[2], context_dictionary)
            elif tokens_list[0] == 'mult':
                return evaluate_expression(tokens_list[1], context_dictionary) * evaluate_expression(tokens_list[2], context_dictionary)
            elif tokens_list[0] == 'let':
                new_context = context_dictionary.copy()
                i = 1
                while i < len(tokens_list) - 1:
                    var = tokens_list[i]
                    expr = tokens_list[i + 1]
                    new_context[var] = evaluate_expression(expr, new_context)
                    i += 2
                return evaluate_expression(tokens_list[-1], new_context)

        def parse_expression(expression_string: str):
            if not expression_string or expression_string[0] != '(':
                return expression_string
            tokens = get_tokens(expression_string[1:-1])
            return [parse_expression(token) for token in tokens]

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
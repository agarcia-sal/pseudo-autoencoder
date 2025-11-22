class Solution:
    def evaluate(self, expression: str) -> int:
        def get_tokens(expression_string: str) -> list[str]:
            tokens = []
            buffer = ''
            depth = 0
            for ch in expression_string:
                if ch == ' ' and depth == 0:
                    if buffer:
                        tokens.append(buffer)
                        buffer = ''
                else:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                    buffer += ch
            if buffer:
                tokens.append(buffer)
            return tokens

        def parse_expression(expression_string: str):
            if not expression_string or expression_string[0] != '(':
                return expression_string
            tokens = get_tokens(expression_string[1:-1])
            return [parse_expression(token) for token in tokens]

        def evaluate_expression(tokens_list, context_dict):
            if isinstance(tokens_list, str):
                # tokens_list is a string token (not a list)
                try:
                    return int(tokens_list)
                except ValueError:
                    return context_dict[tokens_list]
            op = tokens_list[0]
            if op == 'add':
                return evaluate_expression(tokens_list[1], context_dict) + evaluate_expression(tokens_list[2], context_dict)
            elif op == 'mult':
                return evaluate_expression(tokens_list[1], context_dict) * evaluate_expression(tokens_list[2], context_dict)
            elif op == 'let':
                new_context = context_dict.copy()
                i = 1
                while i < len(tokens_list) - 1:
                    var_name = tokens_list[i]
                    exp_val = tokens_list[i + 1]
                    val = evaluate_expression(exp_val, new_context)
                    new_context[var_name] = val
                    i += 2
                return evaluate_expression(tokens_list[-1], new_context)
            else:
                # fallback: should not reach here normally
                return int(tokens_list[0])

        parsed_expression = parse_expression(expression)
        return evaluate_expression(parsed_expression, {})
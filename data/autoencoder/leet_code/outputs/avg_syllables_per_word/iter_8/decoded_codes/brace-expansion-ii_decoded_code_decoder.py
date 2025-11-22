class Solution:
    def braceExpansionII(self, expression):
        def parse_expression(index):
            current_set = set()
            current_product = ['']

            while index < len(expression):
                char = expression[index]

                if char == '{':
                    inner_set, index = parse_expression(index + 1)
                    current_product = [prefix + suffix for prefix in current_product for suffix in inner_set]

                elif char == '}':
                    current_set.update(current_product)
                    return current_set, index

                elif char == ',':
                    current_set.update(current_product)
                    current_product = ['']

                else:
                    current_product = [prefix + char for prefix in current_product]

                index += 1

            current_set.update(current_product)
            return current_set, index

        result_set, _ = parse_expression(0)
        return sorted(result_set)
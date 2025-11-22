class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expression(index: int):
            current_set = set()
            current_product = ['']

            while index < len(expression):
                char = expression[index]

                if char == '{':
                    inner_set, index = parse_expression(index + 1)
                    # Cartesian product of current_product and inner_set
                    current_product = [a + b for a in current_product for b in inner_set]
                elif char == '}':
                    # Add all strings in current_product to current_set and return
                    current_set.update(current_product)
                    return current_set, index
                elif char == ',':
                    # Add current_product to current_set and reset current_product
                    current_set.update(current_product)
                    current_product = ['']
                else:
                    # Append char to each string in current_product
                    current_product = [a + char for a in current_product]

                index += 1

            # End of expression: add current_product to current_set
            current_set.update(current_product)
            return current_set, index

        result_set, _ = parse_expression(0)
        return sorted(result_set)
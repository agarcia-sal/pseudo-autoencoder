class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expression(index: int) -> tuple[set[str], int]:
            current_set = set()
            current_product = ['']

            while index < len(expression):
                char = expression[index]
                if char == '{':
                    inner_set, index = parse_expression(index + 1)
                    current_product = [prev + cur for prev in current_product for cur in inner_set]
                elif char == '}':
                    current_set.update(current_product)
                    return current_set, index
                elif char == ',':
                    current_set.update(current_product)
                    current_product = ['']
                else:
                    current_product = [prev + char for prev in current_product]
                index += 1

            current_set.update(current_product)
            return current_set, index

        result_set, _ = parse_expression(0)
        return sorted(result_set)
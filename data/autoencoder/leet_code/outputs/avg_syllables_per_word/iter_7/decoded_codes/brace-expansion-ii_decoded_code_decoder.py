from typing import Tuple, Set, List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse_expression(index: int) -> Tuple[Set[str], int]:
            current_set: Set[str] = set()
            current_product: List[str] = ['']

            while index < len(expression):
                char = expression[index]

                if char == '{':
                    inner_set, index = parse_expression(index + 1)
                    new_product: List[str] = []
                    for a in current_product:
                        for b in inner_set:
                            new_product.append(a + b)
                    current_product = new_product

                elif char == '}':
                    current_set.update(current_product)
                    return current_set, index

                elif char == ',':
                    current_set.update(current_product)
                    current_product = ['']

                else:
                    updated_product: List[str] = []
                    for a in current_product:
                        updated_product.append(a + char)
                    current_product = updated_product

                index += 1

            current_set.update(current_product)
            return current_set, index

        result_set, _ = parse_expression(0)
        return sorted(result_set)
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expression(index: int):
            current_set = set()
            current_product = ['']
            while index < len(expression):
                char = expression[index]
                if char == '{':
                    inner_set, index = parse_expression(index + 1)
                    new_product = []
                    for a in current_product:
                        for b in inner_set:
                            new_product.append(a + b)
                    current_product = new_product
                elif char == '}':
                    for s in current_product:
                        current_set.add(s)
                    return current_set, index
                elif char == ',':
                    for s in current_product:
                        current_set.add(s)
                    current_product = ['']
                else:
                    new_product = []
                    for a in current_product:
                        new_product.append(a + char)
                    current_product = new_product
                index += 1
            for s in current_product:
                current_set.add(s)
            return current_set, index
        result_set, _ = parse_expression(0)
        return sorted(result_set)
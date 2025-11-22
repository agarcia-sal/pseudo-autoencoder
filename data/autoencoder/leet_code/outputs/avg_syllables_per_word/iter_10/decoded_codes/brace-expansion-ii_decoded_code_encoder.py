class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expression(i):
            current_set = set()
            current_product = ['']
            while i < len(expression):
                char = expression[i]
                if char == '{':
                    inner_set, i = parse_expression(i + 1)
                    new_product = []
                    for a in current_product:
                        for b in inner_set:
                            new_product.append(a + b)
                    current_product = new_product
                elif char == '}':
                    for p in current_product:
                        current_set.add(p)
                    return current_set, i
                elif char == ',':
                    for p in current_product:
                        current_set.add(p)
                    current_product = ['']
                else:
                    current_product = [p + char for p in current_product]
                i += 1
            for p in current_product:
                current_set.add(p)
            return current_set, i

        result_set, _ = parse_expression(0)
        return sorted(result_set)
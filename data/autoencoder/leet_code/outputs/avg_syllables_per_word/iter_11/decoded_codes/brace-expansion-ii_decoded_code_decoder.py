class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expression(index: int) -> tuple[set[str], int]:
            current_set = set()
            current_product = ['']
            while index < len(expression):
                char = expression[index]
                if char == '{':
                    inner_set, index = parse_expression(index + 1)
                    temp_list = []
                    for a in current_product:
                        for b in inner_set:
                            temp_list.append(a + b)
                    current_product = temp_list
                elif char == '}':
                    for p in current_product:
                        current_set.add(p)
                    return current_set, index
                elif char == ',':
                    for p in current_product:
                        current_set.add(p)
                    current_product = ['']
                else:
                    temp_list = []
                    for a in current_product:
                        temp_list.append(a + char)
                    current_product = temp_list
                index += 1
            for p in current_product:
                current_set.add(p)
            return current_set, index

        result_set, _ = parse_expression(0)
        return sorted(result_set)
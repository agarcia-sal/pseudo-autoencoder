class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index: int):
            # If next character is ':' or at the last character, return current char and next index
            if index == len(expression) - 1 or expression[index + 1] == ':':
                return expression[index], index + 2

            true_part, next_index = evaluate(index + 2)
            false_part, final_index = evaluate(next_index)

            if expression[index] == 'T':
                return true_part, final_index
            else:
                return false_part, final_index

        result, _ = evaluate(0)
        return result
class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(pos: int):
            # Base case: if next character is ':' or we're at the last char, return current char and next position
            if pos == len(expression) - 1 or (pos + 1 < len(expression) and expression[pos + 1] == ':'):
                return expression[pos], pos + 2

            true_part, updated_pos = evaluate(pos + 2)
            false_part, final_pos = evaluate(updated_pos)

            if expression[pos] == 'T':
                return true_part, final_pos
            else:
                return false_part, final_pos

        result, _ = evaluate(0)
        return result
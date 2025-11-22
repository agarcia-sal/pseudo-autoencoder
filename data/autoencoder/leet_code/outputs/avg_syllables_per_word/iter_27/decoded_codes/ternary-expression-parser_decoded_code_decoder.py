class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index: int) -> tuple[str, int]:
            if index == len(expression) - 1 or (index + 1 < len(expression) and expression[index + 1] == ':'):
                return expression[index], index + 1
            true_part, next_index = evaluate(index + 2)
            false_part, final_index = evaluate(next_index)
            return (true_part if expression[index] == 'T' else false_part, final_index)

        result, _ = evaluate(0)
        return result
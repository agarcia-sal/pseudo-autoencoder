class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index: int):
            # Base case: if at last character or next character is ':', return current char and advance by 2
            if index == len(expression) - 1 or expression[index + 1] == ':':
                return expression[index], index + 2
            # Recursively evaluate the 'true' part and its next index
            true_part, next_index = evaluate(index + 2)
            # Recursively evaluate the 'false' part and final index
            false_part, final_index = evaluate(next_index)
            # Decide which part to return based on the current condition character
            if expression[index] == 'T':
                return true_part, final_index
            else:
                return false_part, final_index

        result, _ = evaluate(0)
        return result
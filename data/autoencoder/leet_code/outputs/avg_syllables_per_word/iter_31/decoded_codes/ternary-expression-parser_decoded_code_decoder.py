from typing import Tuple

class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index: int) -> Tuple[str, int]:
            # If last character or next is ':', return the current character and index+2 (skip ":")
            if index == len(expression) - 1 or expression[index + 1] == ':':
                return expression[index], index + 2
            # Recursively evaluate true part (after '?')
            true_part, next_index = evaluate(index + 2)
            # Recursively evaluate false part
            false_part, final_index = evaluate(next_index)
            # Return value based on current condition character 'T' or 'F'
            if expression[index] == 'T':
                return true_part, final_index
            else:
                return false_part, final_index

        result, _ = evaluate(0)
        return result
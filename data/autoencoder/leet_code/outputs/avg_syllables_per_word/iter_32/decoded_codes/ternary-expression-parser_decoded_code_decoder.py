from typing import Tuple

class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index: int) -> Tuple[str, int]:
            # If at the last character or next character is ':', this is a leaf node
            if index == len(expression) - 1 or (index + 1 < len(expression) and expression[index + 1] == ':'):
                return expression[index], index + 2
            # Otherwise, expression[index] is 'T' or 'F', and structure like: condition?true_part:false_part
            true_part, next_index = evaluate(index + 2)   # evaluate true part (after '?')
            false_part, final_index = evaluate(next_index) # evaluate false part (after ':')
            if expression[index] == 'T':
                return true_part, final_index
            else:
                return false_part, final_index

        result, _ = evaluate(0)
        return result
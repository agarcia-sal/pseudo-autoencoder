from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current_string: str = '', left_count: int = 0, right_count: int = 0) -> None:
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            if left_count < n:
                backtrack(current_string + '(', left_count + 1, right_count)
            if right_count < left_count:
                backtrack(current_string + ')', left_count, right_count + 1)

        result: List[str] = []
        backtrack()
        return result
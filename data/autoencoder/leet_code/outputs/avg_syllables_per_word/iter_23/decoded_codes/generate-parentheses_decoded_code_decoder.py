from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s: str = "", left: int = 0, right: int = 0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack()
        return result
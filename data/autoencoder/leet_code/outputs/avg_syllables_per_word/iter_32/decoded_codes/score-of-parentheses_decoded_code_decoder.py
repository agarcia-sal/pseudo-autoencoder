from typing import List

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack: List[int] = []
        score = 0
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:  # char == ')'
                prev = stack.pop()
                score = prev + (1 if score == 0 else 2 * score)
        return score
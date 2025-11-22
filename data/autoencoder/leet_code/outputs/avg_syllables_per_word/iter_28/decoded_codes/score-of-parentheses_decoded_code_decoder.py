from typing import List

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack: List[int] = []
        score = 0
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                prev_score = stack.pop()
                if score == 0:
                    score = prev_score + 1
                else:
                    score = prev_score + 2 * score
        return score
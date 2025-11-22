class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                last_score = stack.pop()
                if score == 0:
                    score = last_score + 1
                else:
                    score = last_score + 2 * score
        return score
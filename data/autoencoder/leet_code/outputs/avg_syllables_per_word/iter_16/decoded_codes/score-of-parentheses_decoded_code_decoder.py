class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                popped_value = stack.pop()
                if score == 0:
                    score = popped_value + 1
                else:
                    score = popped_value + 2 * score
        return score
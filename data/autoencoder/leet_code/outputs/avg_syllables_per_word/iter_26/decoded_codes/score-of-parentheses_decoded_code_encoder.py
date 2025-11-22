class Solution:
    def scoreOfParentheses(self, string_s: str) -> int:
        stack = []
        score = 0
        for character in string_s:
            if character == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + (1 if score == 0 else 2 * score)
        return score
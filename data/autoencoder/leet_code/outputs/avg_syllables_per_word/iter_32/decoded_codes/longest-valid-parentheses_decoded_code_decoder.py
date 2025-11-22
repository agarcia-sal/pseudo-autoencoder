from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # store indices, start with -1 for base comparison
        max_length = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length
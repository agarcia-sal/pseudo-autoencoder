from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack: List[int] = [-1]
        max_length = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    current_length = i - stack[-1]
                    if current_length > max_length:
                        max_length = current_length
        return max_length
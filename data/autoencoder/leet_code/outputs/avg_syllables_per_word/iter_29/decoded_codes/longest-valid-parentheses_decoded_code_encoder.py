class Solution:
    def longestValidParentheses(self, input_string: str) -> int:
        stack = [-1]
        maximum_length = 0
        for index, character in enumerate(input_string):
            if character == '(':
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    current_length = index - stack[-1]
                    if current_length > maximum_length:
                        maximum_length = current_length
        return maximum_length
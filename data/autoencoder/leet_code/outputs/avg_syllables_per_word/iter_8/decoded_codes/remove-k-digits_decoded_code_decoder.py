class Solution:
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k > 0:
            final_stack = stack[:-k]
        else:
            final_stack = stack

        result = ''.join(final_stack).lstrip('0')

        if not result:
            return "0"
        else:
            return result
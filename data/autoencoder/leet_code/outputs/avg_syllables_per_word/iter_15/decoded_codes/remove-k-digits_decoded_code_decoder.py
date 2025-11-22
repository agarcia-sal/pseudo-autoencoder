class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
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
        return result if result else '0'
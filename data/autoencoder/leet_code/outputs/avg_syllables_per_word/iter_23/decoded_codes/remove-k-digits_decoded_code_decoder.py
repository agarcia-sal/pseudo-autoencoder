class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k == 0:
            final_stack = stack
        else:
            final_stack = stack[:len(stack) - k]

        result = "".join(final_stack).lstrip('0')
        if result:
            return result
        else:
            return "0"
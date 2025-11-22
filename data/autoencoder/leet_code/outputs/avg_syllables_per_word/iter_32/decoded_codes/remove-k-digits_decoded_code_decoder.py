from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack: List[str] = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # If k is still greater than zero, remove from the end
        final_stack = stack if k == 0 else stack[:-k]
        # Join and strip leading zeros
        result = ''.join(final_stack).lstrip('0')
        return result if result else '0'
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.isqrt(c))  # isqrt gives the integer square root directly
        while left <= right:
            current_sum = left * left + right * right
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        return False
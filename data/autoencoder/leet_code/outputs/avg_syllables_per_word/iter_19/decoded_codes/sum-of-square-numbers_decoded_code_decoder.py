import math

class Solution:
    def judgeSquareSum(self, c):
        left = 0
        right = int(math.isqrt(c))  # math.isqrt gives int sqrt without float inaccuracies
        while left <= right:
            current_sum = left * left + right * right
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        return False
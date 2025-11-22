import math

def judgeSquareSum(c):
    left, right = 0, math.isqrt(c)
    while left <= right:
        sum_ = left * left + right * right
        if sum_ == c:
            return True
        if sum_ < c:
            left += 1
        else:
            right -= 1
    return False
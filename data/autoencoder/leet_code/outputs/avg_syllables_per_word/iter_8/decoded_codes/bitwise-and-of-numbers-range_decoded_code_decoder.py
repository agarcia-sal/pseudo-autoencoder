class Solution:
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        while left < right:
            left //= 2
            right //= 2
            shift += 1
        return left * (2 ** shift)
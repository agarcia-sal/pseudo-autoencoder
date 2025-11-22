class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left //= 2
            right //= 2
            shift += 1
        result = left * (2 ** shift)
        return result
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Shift left and right rightwards until they are equal
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
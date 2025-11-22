class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 2147483647
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # largest 32-bit positive integer
        mask = 0xFFFFFFFF  # 32-bit mask

        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry & mask

        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)
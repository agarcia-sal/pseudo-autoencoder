class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # 2^31 - 1
        mask = 0xFFFFFFFF  # 32 bits all set to 1

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)
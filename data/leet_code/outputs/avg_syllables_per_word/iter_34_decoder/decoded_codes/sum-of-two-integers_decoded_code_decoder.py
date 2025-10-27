class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # Maximum positive 32-bit integer
        mask = 0xFFFFFFFF  # 32-bit mask with all bits set to 1

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)
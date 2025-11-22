class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit integer max
        maximum = 0x7FFFFFFF
        # 32-bit mask
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= maximum:
            return a
        else:
            return ~((a & mask) ^ mask)
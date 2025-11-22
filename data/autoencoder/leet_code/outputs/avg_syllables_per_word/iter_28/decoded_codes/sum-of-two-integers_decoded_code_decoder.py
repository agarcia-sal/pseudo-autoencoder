class Solution:
    def getSum(self, a: int, b: int) -> int:
        maximum = 0x7FFFFFFF
        bit_mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & bit_mask
            b = carry & bit_mask

        if a <= maximum:
            return a
        else:
            return ~(a ^ bit_mask)
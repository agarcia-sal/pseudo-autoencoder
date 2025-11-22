class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF  # Maximum 32-bit signed integer
        MASK = 0xFFFFFFFF     # Mask for 32 bits

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)
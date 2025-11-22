class Solution:
    def getSum(self, a, b):
        MAX = 0x7FFFFFFF  # Max positive 32-bit integer
        MASK = 0xFFFFFFFF  # 32-bit mask

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX else ~(a ^ MASK)
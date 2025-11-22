class Solution:
    def getSum(self, a, b):
        max_int = 0x7FFFFFFF  # maximum 32-bit integer
        mask = 0xFFFFFFFF     # mask for 32 bits

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # max positive 32-bit int
        mask = 0xFFFFFFFF  # mask to get last 32 bits
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= MAX else ~(a ^ mask)
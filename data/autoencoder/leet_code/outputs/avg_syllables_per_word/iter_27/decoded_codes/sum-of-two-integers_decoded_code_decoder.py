class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # Maximum positive 32-bit integer (2**31 - 1)
        mask = 0xFFFFFFFF  # Mask to get 32 bits
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= MAX else ~(a ^ mask)
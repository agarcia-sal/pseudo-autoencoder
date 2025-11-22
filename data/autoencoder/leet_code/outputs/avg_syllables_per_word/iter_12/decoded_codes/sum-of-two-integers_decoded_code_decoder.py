class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # Maximum positive 32-bit integer
        mask = 0xFFFFFFFF  # Mask to get last 32 bits

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= MAX else ~(a ^ mask)
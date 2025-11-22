class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # maximum 32-bit signed integer
        mask = 0xFFFFFFFF  # 32 bits set to 1
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= MAX else ~(a ^ mask)
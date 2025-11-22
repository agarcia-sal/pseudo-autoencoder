class Solution:
    def getSum(self, a: int, b: int) -> int:
        maximum = 0x7FFFFFFF  # largest 32-bit integer
        mask = 0xFFFFFFFF     # 32 bits all set to one

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= maximum:
            return a
        else:
            return ~ (a ^ mask)
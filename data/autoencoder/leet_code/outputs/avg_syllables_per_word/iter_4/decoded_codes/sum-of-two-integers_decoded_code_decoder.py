class Solution:
    def getSum(self, a, b):
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)
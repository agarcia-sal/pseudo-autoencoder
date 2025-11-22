class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 7 * 16**7 + 15 * 16**6 + 15 * 16**5 + 15 * 16**4 + 15 * 16**3 + 15 * 16**2 + 15 * 16 + 15
        mask = 15 * 16**7 + 15 * 16**6 + 15 * 16**5 + 15 * 16**4 + 15 * 16**3 + 15 * 16**2 + 15 * 16 + 15 * 16 + 15
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)
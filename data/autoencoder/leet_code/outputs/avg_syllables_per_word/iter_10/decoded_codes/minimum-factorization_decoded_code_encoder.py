class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1

        factors = []
        for digit in range(9, 1, -1):
            while num % digit == 0:
                factors.append(digit)
                num //= digit

        if num != 1:
            return 0

        factors.sort()
        result = int(''.join(map(str, factors)))
        return result if result <= 2**31 - 1 else 0
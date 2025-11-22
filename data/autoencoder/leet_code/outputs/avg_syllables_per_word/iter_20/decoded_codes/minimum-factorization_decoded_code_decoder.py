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
        # Form the result integer by concatenating factors as strings
        result_str = ''.join(str(d) for d in factors)
        result = int(result_str)

        if result > (2 ** 31 - 1):
            return 0

        return result
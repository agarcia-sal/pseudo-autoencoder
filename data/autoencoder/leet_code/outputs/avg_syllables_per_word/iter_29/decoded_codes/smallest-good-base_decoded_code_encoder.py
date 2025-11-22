import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        integer_n = int(n)
        maximum_length = int(math.log2(integer_n)) + 1

        for m in range(maximum_length, 1, -1):
            # Compute candidate base using exponential and logarithms for precision
            candidate_base = int(integer_n ** (1 / (m - 1)))
            if candidate_base < 2:
                continue

            # geometric sum = (candidate_base^m - 1) // (candidate_base - 1)
            geometric_sum = (pow(candidate_base, m) - 1) // (candidate_base - 1)
            if geometric_sum == integer_n:
                return str(candidate_base)

        return str(integer_n - 1)
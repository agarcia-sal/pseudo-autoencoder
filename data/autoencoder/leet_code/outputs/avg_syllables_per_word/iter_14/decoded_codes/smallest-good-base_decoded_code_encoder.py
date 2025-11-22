import math

class Solution:
    def smallestGoodBase(self, n_as_string: str) -> str:
        n = int(n_as_string)
        max_length = int(math.log2(n)) + 1

        for m in range(max_length, 1, -1):
            k = int(n ** (1 / (m - 1)))
            if k < 2:
                continue
            numerator = pow(k, m) - 1
            denominator = k - 1
            num = numerator // denominator
            if num == n:
                return str(k)

        return str(n - 1)
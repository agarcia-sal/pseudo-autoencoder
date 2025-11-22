import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n_int = int(n)
        max_length = int(math.log2(n_int)) + 1

        for m in range(max_length, 1, -1):
            k = int(n_int ** (1 / (m - 1)))
            if k < 2:
                continue

            # Compute sum of geometric series: 1 + k + k^2 + ... + k^(m-1)
            # Use formula: (k^m - 1) // (k - 1)
            numerator = pow(k, m) - 1
            denominator = k - 1
            if numerator // denominator == n_int and numerator % denominator == 0:
                return str(k)

        return str(n_int - 1)
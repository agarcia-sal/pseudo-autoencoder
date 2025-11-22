import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n_int = int(n)
        max_length = int(math.log2(n_int)) + 1
        for m in range(max_length, 1, -1):
            k = int(n_int ** (1 / (m - 1)))
            if k < 2:
                continue
            # Calculate sum of geometric series: (k^m - 1) // (k - 1)
            # Use pow with three arguments to avoid large intermediate results overflow is not a concern for int
            num = (pow(k, m) - 1) // (k - 1)
            if num == n_int:
                return str(k)
        return str(n_int - 1)
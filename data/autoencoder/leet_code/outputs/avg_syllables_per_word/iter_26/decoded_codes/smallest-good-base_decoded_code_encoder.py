import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_len = int(math.log2(n)) + 1
        for m in range(max_len, 1, -1):
            k = int(n ** (1 / (m - 1)))
            if k < 2:
                continue
            # Use geometric series sum formula: (k^m - 1)//(k - 1)
            geometric_sum = (k ** m - 1) // (k - 1)
            if geometric_sum == n:
                return str(k)
        return str(n - 1)
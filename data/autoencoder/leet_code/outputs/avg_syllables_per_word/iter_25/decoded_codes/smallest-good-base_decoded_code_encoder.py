import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n_int = int(n)
        max_length = int(math.log2(n_int)) + 1
        for m in range(max_length, 1, -1):
            k = int(n_int ** (1 / m)) - 1
            if k < 2:
                continue
            # compute (k^(m+1) - 1) // (k - 1)
            num = (pow(k, m + 1) - 1) // (k - 1)
            if num == n_int:
                return str(k)
        return str(n_int - 1)
import math

class Solution:
    def smallestGoodBase(self, n):
        n = int(n)
        max_length = int(math.log2(n)) + 1

        for m in range(max_length, 1, -1):
            k = int(n ** (1 / (m - 1)))
            if k < 2:
                continue

            num = (k ** m - 1) // (k - 1)
            if num == n:
                return str(k)
        return str(n - 1)
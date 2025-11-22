import math
from functools import lru_cache
from math import comb

class Solution:
    def getProbability(self, balls):
        n = sum(balls) // 2
        k = len(balls)

        @lru_cache(None)
        def dfs(i, j, diff):
            if i >= k:
                return 1 if j == 0 and diff == 0 else 0
            if j < 0:
                return 0

            ans = 0
            total = balls[i]
            for x in range(total + 1):
                if x == total:
                    y = 1
                elif x == 0:
                    y = -1
                else:
                    y = 0
                ans += dfs(i + 1, j - x, diff + y) * comb(total, x)
            return ans

        total_comb = comb(2 * n, n)
        return dfs(0, n, 0) / total_comb
from math import comb
from functools import lru_cache

class Solution:
    def getProbability(self, balls):
        n = sum(balls) >> 1
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

        return dfs(0, n, 0) / comb(sum(balls), n)
from math import comb
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        k = len(balls)
        n = sum(balls) // 2

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, diff: int) -> float:
            if i >= k:
                return 1.0 if j == 0 and diff == 0 else 0.0
            if j < 0:
                return 0.0
            ans = 0.0
            total_balls_i = balls[i]
            for x in range(total_balls_i + 1):
                if x == total_balls_i:
                    y = 1
                elif x == 0:
                    y = -1
                else:
                    y = 0
                ans += dfs(i + 1, j - x, diff + y) * comb(total_balls_i, x)
            return ans

        return dfs(0, n, 0) / comb(n * 2, n)
from math import comb
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        total_balls = sum(balls)
        n = total_balls // 2
        k = len(balls)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, diff: int) -> float:
            if i >= k:
                return 1.0 if j == 0 and diff == 0 else 0.0
            if j < 0:
                return 0.0

            ans = 0.0
            balls_i = balls[i]
            for x in range(balls_i + 1):
                if x == balls_i:
                    y = 1
                elif x == 0:
                    y = -1
                else:
                    y = 0
                ans += dfs(i + 1, j - x, diff + y) * comb(balls_i, x)
            return ans

        return dfs(0, n, 0) / comb(total_balls, n)
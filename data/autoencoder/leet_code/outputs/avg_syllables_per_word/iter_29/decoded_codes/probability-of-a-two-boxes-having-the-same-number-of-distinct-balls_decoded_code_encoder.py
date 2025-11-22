import math
from functools import lru_cache
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2
        k = len(balls)

        # Precompute factorials for combinations to optimize repeated calls
        fact = [1]
        for i in range(1, sum(balls) + 1):
            fact.append(fact[-1] * i)

        def comb(n: int, r: int) -> int:
            if r > n or r < 0:
                return 0
            return fact[n] // (fact[r] * fact[n - r])

        @lru_cache(None)
        def dfs(i: int, j: int, diff: int) -> int:
            if i >= k:
                return 1 if j == 0 and diff == 0 else 0
            if j < 0:
                return 0
            ans = 0
            ball_count = balls[i]
            for x in range(ball_count + 1):
                if x == ball_count:
                    y = 1
                elif x == 0:
                    y = -1
                else:
                    y = 0
                ans += dfs(i + 1, j - x, diff + y) * comb(ball_count, x)
            return ans

        total_comb = comb(sum(balls), n)
        return dfs(0, n, 0) / total_comb
from math import comb
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2
        k = len(balls)

        def dfs(i: int, j: int, diff: int) -> float:
            if i >= k:
                if j == 0 and diff == 0:
                    return 1
                else:
                    return 0
            if j < 0:
                return 0
            ans = 0
            for x in range(balls[i] + 1):
                if x == balls[i]:
                    y = 1
                elif x == 0:
                    y = -1
                else:
                    y = 0
                ans += dfs(i + 1, j - x, diff + y) * comb(balls[i], x)
            return ans

        return dfs(0, n, 0) / comb(n * 2, n)
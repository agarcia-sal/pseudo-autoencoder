from math import inf
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0]) if m > 0 else 0
        # dp dimensions: (m+1) x (n+1), initialized to infinity
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(min_health, 1)
        return dp[0][0]
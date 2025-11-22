from functools import cache

class Solution:
    def stoneGame(self, piles):
        @cache
        def dfs(i, j):
            if i > j:
                return 0
            value_from_left = piles[i] - dfs(i + 1, j)
            value_from_right = piles[j] - dfs(i, j - 1)
            return value_from_left if value_from_left > value_from_right else value_from_right

        result = dfs(0, len(piles) - 1) > 0
        return result
class Solution:
    def stoneGame(self, piles):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            left_choice = piles[i] - dfs(i + 1, j)
            right_choice = piles[j] - dfs(i, j - 1)
            return left_choice if left_choice > right_choice else right_choice

        return dfs(0, len(piles) - 1) > 0
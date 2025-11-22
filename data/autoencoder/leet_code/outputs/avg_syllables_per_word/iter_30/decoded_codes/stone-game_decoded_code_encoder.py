from functools import lru_cache

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            return max(piles[i] - dfs(i + 1, j), piles[j] - dfs(i, j - 1))
        return dfs(0, len(piles) - 1) > 0
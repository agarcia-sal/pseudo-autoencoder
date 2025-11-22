from functools import lru_cache

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            score_from_left = piles[i] - dfs(i + 1, j)
            score_from_right = piles[j] - dfs(i, j - 1)
            return max(score_from_left, score_from_right)

        result = dfs(0, len(piles) - 1)
        return result > 0
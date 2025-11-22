from functools import lru_cache
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            left = piles[i] - dfs(i + 1, j)
            right = piles[j] - dfs(i, j - 1)
            return max(left, right)

        return dfs(0, len(piles) - 1) > 0
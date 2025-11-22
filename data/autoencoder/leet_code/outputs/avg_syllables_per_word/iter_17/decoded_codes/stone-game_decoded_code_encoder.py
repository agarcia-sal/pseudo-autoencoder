from functools import cache
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            left_choice = piles[i] - dfs(i + 1, j)
            right_choice = piles[j] - dfs(i, j - 1)
            return max(left_choice, right_choice)

        result = dfs(0, len(piles) - 1)
        return result > 0
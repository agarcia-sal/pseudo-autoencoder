from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            left_choice = piles[i] - dfs(i + 1, j)
            right_choice = piles[j] - dfs(i, j - 1)
            return left_choice if left_choice > right_choice else right_choice

        result = dfs(0, len(piles) - 1)
        return result > 0
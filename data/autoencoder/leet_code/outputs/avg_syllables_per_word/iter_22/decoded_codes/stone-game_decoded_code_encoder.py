from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            result_from_left = piles[i] - dfs(i + 1, j)
            result_from_right = piles[j] - dfs(i, j - 1)
            return max(result_from_left, result_from_right)
        final_result = dfs(0, len(piles) - 1)
        return final_result > 0
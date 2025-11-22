from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            left = piles[i] - dfs(i + 1, j)
            right = piles[j] - dfs(i, j - 1)
            memo[(i, j)] = max(left, right)
            return memo[(i, j)]

        return dfs(0, len(piles) - 1) > 0
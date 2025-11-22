from math import inf
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, d_remaining: int) -> int:
            if d_remaining == 1:
                return max(jobDifficulty[i:])

            min_diff = inf
            max_difficulty = 0
            # j goes from i to n - d_remaining (inclusive)
            for j in range(i, n - d_remaining + 1):
                max_difficulty = max(max_difficulty, jobDifficulty[j])
                candidate = max_difficulty + dp(j + 1, d_remaining - 1)
                if candidate < min_diff:
                    min_diff = candidate
            return min_diff

        return dp(0, d)
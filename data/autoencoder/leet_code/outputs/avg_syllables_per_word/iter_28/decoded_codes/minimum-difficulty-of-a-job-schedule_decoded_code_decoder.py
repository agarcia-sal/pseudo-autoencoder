from math import inf
from functools import lru_cache
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, d: int) -> int:
            if d == 1:
                return max(jobDifficulty[i:])

            min_difficulty = inf
            current_max = 0
            for j in range(i, n - d + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, d - 1)
                if candidate < min_difficulty:
                    min_difficulty = candidate
            return min_difficulty

        return dp(0, d)
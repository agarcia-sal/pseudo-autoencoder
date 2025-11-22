from math import inf
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, days: int) -> int:
            if days == 1:
                return max(jobDifficulty[i:])
            min_difficulty = inf
            current_max = 0
            for j in range(i, n - days + 1):
                current_max = max(current_max, jobDifficulty[j])
                min_difficulty = min(min_difficulty, current_max + dp(j + 1, days - 1))
            return min_difficulty

        return dp(0, d)
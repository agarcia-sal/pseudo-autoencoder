from math import inf
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, days_remaining: int) -> int:
            if days_remaining == 1:
                return max(jobDifficulty[i:])
            min_difficulty = inf
            current_max = 0
            # j goes up to n - days_remaining because we need at least days_remaining - 1 jobs for remaining days
            for j in range(i, n - days_remaining + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, days_remaining - 1)
                if candidate < min_difficulty:
                    min_difficulty = candidate
            return min_difficulty

        return dp(0, d)
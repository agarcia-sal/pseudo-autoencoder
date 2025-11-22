from math import inf
from functools import lru_cache
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, days: int) -> int:
            if days == 1:
                return max(jobDifficulty[i:]) if i < n else 0

            min_difficulty = inf
            current_max = 0
            # We need to leave at least (days-1) jobs for remaining days,
            # so the last job to consider for current day ends at index n - days
            for j in range(i, n - days + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, days - 1)
                if candidate < min_difficulty:
                    min_difficulty = candidate
            return min_difficulty

        return dp(0, d)
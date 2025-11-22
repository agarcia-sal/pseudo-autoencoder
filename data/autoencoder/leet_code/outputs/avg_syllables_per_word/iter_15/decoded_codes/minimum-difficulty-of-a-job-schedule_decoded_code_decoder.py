from math import inf
from functools import lru_cache
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, day: int) -> int:
            if day == 1:
                return max(jobDifficulty[i:])
            min_difficulty = inf
            current_max = 0
            # j can go up to n - day because we need at least (day-1) jobs after j
            for j in range(i, n - day + 1):
                current_max = max(current_max, jobDifficulty[j])
                min_difficulty = min(min_difficulty, current_max + dp(j + 1, day - 1))
            return min_difficulty

        return dp(0, d)
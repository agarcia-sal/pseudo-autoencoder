from functools import lru_cache
from math import inf

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i, d_remaining):
            if d_remaining == 1:
                return max(jobDifficulty[i:])
            min_difficulty = inf
            current_max = 0
            # j goes up to n - d_remaining because we need to leave at least d_remaining - 1 jobs for the remaining days
            for j in range(i, n - d_remaining + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, d_remaining - 1)
                if candidate < min_difficulty:
                    min_difficulty = candidate
            return min_difficulty

        return dp(0, d)
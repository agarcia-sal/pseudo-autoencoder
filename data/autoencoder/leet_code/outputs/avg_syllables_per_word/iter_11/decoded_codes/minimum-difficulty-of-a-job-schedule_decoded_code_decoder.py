from math import inf
from functools import cache

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        @cache
        def dp(i, d_left):
            if d_left == 1:
                return max(jobDifficulty[i:])
            min_difficulty = inf
            current_max = 0
            for j in range(i, n - d_left + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, d_left - 1)
                min_difficulty = min(min_difficulty, candidate)
            return min_difficulty

        return dp(0, d)
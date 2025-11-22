from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i, days_left):
            if days_left == 1:
                return max(jobDifficulty[i:])
            min_diff = float('inf')
            curr_max = 0
            for j in range(i, n - days_left + 1):
                curr_max = max(curr_max, jobDifficulty[j])
                min_diff = min(min_diff, curr_max + dp(j + 1, days_left - 1))
            return min_diff

        return dp(0, d)
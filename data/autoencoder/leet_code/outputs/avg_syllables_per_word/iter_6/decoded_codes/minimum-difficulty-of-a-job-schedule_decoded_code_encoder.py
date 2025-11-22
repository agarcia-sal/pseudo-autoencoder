class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, days):
            if days == 1:
                return max(jobDifficulty[i:])

            min_difficulty = float('inf')
            current_max = 0
            for j in range(i, n - days + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, days - 1)
                if candidate < min_difficulty:
                    min_difficulty = candidate

            return min_difficulty

        return dp(0, d)
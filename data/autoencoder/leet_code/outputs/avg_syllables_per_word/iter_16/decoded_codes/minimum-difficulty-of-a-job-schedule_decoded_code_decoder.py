from math import inf

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, day):
            if day == 1:
                return max(jobDifficulty[i:])

            min_difficulty = inf
            current_max = 0
            # Ensure partition leaves enough jobs for remaining days
            for j in range(i, n - day + 1):
                current_max = max(current_max, jobDifficulty[j])
                next_difficulty = dp(j + 1, day - 1)
                min_difficulty = min(min_difficulty, current_max + next_difficulty)

            return min_difficulty

        return dp(0, d)
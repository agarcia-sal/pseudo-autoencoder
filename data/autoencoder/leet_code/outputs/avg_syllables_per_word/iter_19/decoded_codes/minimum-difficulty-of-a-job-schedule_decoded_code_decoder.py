from math import inf

class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, d_remain: int) -> int:
            if d_remain == 1:
                return max(jobDifficulty[i:])

            min_difficulty = inf
            current_max = 0
            # The last job index we can assign on current day is n - d_remain
            for j in range(i, n - d_remain + 1):
                current_max = max(current_max, jobDifficulty[j])
                next_day_difficulty = dp(j + 1, d_remain - 1)
                min_difficulty = min(min_difficulty, current_max + next_day_difficulty)

            return min_difficulty

        return dp(0, d)
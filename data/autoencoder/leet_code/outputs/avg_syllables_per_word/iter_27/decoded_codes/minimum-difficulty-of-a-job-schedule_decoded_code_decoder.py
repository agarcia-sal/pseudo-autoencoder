from math import inf
from functools import lru_cache
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, remaining_days: int) -> int:
            if remaining_days == 1:
                return max(jobDifficulty[i:]) if i < n else -1

            min_difficulty = inf
            current_max = 0
            # i <= j <= n - remaining_days
            for j in range(i, n - remaining_days + 1):
                current_max = max(current_max, jobDifficulty[j])
                next_difficulty = dp(j + 1, remaining_days - 1)
                if next_difficulty != -1:
                    min_difficulty = min(min_difficulty, current_max + next_difficulty)

            return min_difficulty if min_difficulty != inf else -1

        return dp(0, d)
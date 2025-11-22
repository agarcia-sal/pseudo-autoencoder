from typing import List
import math
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, remaining_days: int) -> int:
            if remaining_days == 1:
                return max(jobDifficulty[i:])

            min_difficulty = math.inf
            current_max = 0
            # The last job for the current day can be at position n - remaining_days
            for j in range(i, n - remaining_days + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate_difficulty = current_max + dp(j + 1, remaining_days - 1)
                min_difficulty = min(min_difficulty, candidate_difficulty)
            return min_difficulty

        return dp(0, d)
from typing import List
from functools import lru_cache
import math

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, days: int) -> int:
            if days == 1:
                return max(jobDifficulty[i:])

            min_difficulty = math.inf
            current_max = 0
            # The last possible j is n - days to ensure at least (days-1) job groups after j
            for j in range(i, n - days + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, days - 1)
                min_difficulty = min(min_difficulty, candidate)
            return min_difficulty

        return dp(0, d)
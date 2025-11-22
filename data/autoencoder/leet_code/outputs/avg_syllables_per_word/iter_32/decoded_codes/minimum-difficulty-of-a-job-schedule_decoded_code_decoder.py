from typing import List
import math
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dp(i: int, day_count: int) -> int:
            if day_count == 1:
                return max(jobDifficulty[i:])

            min_difficulty = math.inf
            current_max = 0
            # j can go up to n - day_count so that there are enough jobs left for remaining days
            for j in range(i, n - day_count + 1):
                current_max = max(current_max, jobDifficulty[j])
                candidate = current_max + dp(j + 1, day_count - 1)
                if candidate < min_difficulty:
                    min_difficulty = candidate
            return min_difficulty

        return dp(0, d)
from typing import List, Tuple
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        @lru_cache(None)
        def dp(remainder: int, *remainder_count_params: int) -> int:
            remainder_count_list = list(remainder_count_params)
            max_happy = 0
            for i in range(batchSize):
                if remainder_count_list[i] == 0:
                    continue
                remainder_count_list[i] -= 1
                new_remainder = (remainder - i) % batchSize
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, *remainder_count_list)
                else:
                    happy_groups = dp(new_remainder, *remainder_count_list)
                if happy_groups > max_happy:
                    max_happy = happy_groups
                remainder_count_list[i] += 1
            return max_happy

        return dp(0, *remainder_count)
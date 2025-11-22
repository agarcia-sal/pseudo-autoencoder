from functools import lru_cache
from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        # Pre-handle groups with zero remainder, they are always happy:
        initial_happy = remainder_count[0]
        remainder_count[0] = 0  # will handle them separately

        @lru_cache(None)
        def dp(remainder: int, *counts: int) -> int:
            counts_list = list(counts)
            max_happy = 0
            for i in range(batchSize):
                if counts_list[i] == 0:
                    continue
                counts_list[i] -= 1
                new_remainder = (remainder - i) % batchSize
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, *counts_list)
                else:
                    happy_groups = dp(new_remainder, *counts_list)
                max_happy = max(max_happy, happy_groups)
                counts_list[i] += 1
            return max_happy

        return initial_happy + dp(0, *remainder_count)
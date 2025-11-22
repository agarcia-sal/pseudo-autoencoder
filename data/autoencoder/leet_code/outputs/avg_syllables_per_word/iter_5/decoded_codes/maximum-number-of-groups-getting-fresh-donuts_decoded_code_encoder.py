from functools import cache
from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for g in groups:
            remainder_count[g % batchSize] += 1

        @cache
        def dp(remainder: int, counts: tuple) -> int:
            max_happy = 0
            counts_list = list(counts)
            for i in range(batchSize):
                if counts_list[i] == 0:
                    continue
                counts_list[i] -= 1
                new_remainder = (remainder - i) % batchSize
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, tuple(counts_list))
                else:
                    happy_groups = dp(new_remainder, tuple(counts_list))
                max_happy = max(max_happy, happy_groups)
                counts_list[i] += 1
            return max_happy

        return dp(0, tuple(remainder_count))
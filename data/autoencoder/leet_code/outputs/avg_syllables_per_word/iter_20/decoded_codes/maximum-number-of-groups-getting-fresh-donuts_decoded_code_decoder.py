from functools import cache
from typing import List, Tuple

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        # dp caches previous computations with remainder and tuple of counts
        @cache
        def dp(remainder: int, remainder_count_tuple: Tuple[int, ...]) -> int:
            remainder_count = list(remainder_count_tuple)
            max_happy = 0

            for i in range(batchSize):
                if remainder_count[i] == 0:
                    continue
                remainder_count[i] -= 1

                new_remainder = (remainder - i) % batchSize

                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, tuple(remainder_count))
                else:
                    happy_groups = dp(new_remainder, tuple(remainder_count))

                max_happy = max(max_happy, happy_groups)
                remainder_count[i] += 1

            return max_happy

        return dp(0, tuple(remainder_count))
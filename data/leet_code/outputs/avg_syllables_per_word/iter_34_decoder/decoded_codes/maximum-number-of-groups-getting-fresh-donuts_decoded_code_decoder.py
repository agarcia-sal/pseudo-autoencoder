from functools import cache
from math import floor
from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_index = group - (group // batchSize) * batchSize
            remainder_count[remainder_index] += 1

        # Convert to tuple for caching, since list is not hashable
        @cache
        def dp(remainder: int, *counts: int) -> int:
            remainder_count = list(counts)
            max_happy = 0

            for index in range(batchSize):
                if remainder_count[index] == 0:
                    continue
                remainder_count[index] -= 1

                new_remainder = remainder - index + batchSize * 2  # ensure positive
                new_remainder -= (new_remainder // batchSize) * batchSize

                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, *remainder_count)
                else:
                    happy_groups = dp(new_remainder, *remainder_count)

                if happy_groups > max_happy:
                    max_happy = happy_groups

                remainder_count[index] += 1

            return max_happy

        return dp(0, *remainder_count)
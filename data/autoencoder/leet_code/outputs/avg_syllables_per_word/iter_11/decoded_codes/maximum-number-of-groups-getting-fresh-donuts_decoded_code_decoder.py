from functools import cache
from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        @cache
        def dp(remainder: int, *remainder_count_elements: int) -> int:
            remain = list(remainder_count_elements)
            max_happy = 0

            for i in range(batchSize):
                if remain[i] == 0:
                    continue
                remain[i] -= 1
                new_remainder = (remainder - i) % batchSize
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, *remain)
                else:
                    happy_groups = dp(new_remainder, *remain)
                max_happy = max(max_happy, happy_groups)
                remain[i] += 1

            return max_happy

        return dp(0, *remainder_count)
from functools import lru_cache
from typing import List, Tuple

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # If batchSize is 1, every group is happy
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        # Convert list to tuple for caching and copy for manipulation inside dp
        @lru_cache(None)
        def dp(remainder: int, remainder_count: Tuple[int, ...]) -> int:
            max_happy = 0
            remainder_count_list = list(remainder_count)

            for i in range(batchSize):
                if remainder_count_list[i] == 0:
                    continue

                remainder_count_list[i] -= 1
                new_remainder = (remainder - i) % batchSize

                # If current remainder is zero, the current group makes a new happy group
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, tuple(remainder_count_list))
                else:
                    happy_groups = dp(new_remainder, tuple(remainder_count_list))

                if happy_groups > max_happy:
                    max_happy = happy_groups

                remainder_count_list[i] += 1

            return max_happy

        return dp(0, tuple(remainder_count))
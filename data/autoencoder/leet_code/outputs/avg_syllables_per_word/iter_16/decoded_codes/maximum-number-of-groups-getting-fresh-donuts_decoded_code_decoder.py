from typing import List
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        # Remove zero remainder groups, they always form happy groups individually
        # but since remainder=0 handled in dp, just count them now:
        happy = remainder_count[0]
        remainder_count[0] = 0

        @lru_cache(None)
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
                if happy_groups > max_happy:
                    max_happy = happy_groups
                counts_list[i] += 1

            return max_happy

        return happy + dp(0, tuple(remainder_count))
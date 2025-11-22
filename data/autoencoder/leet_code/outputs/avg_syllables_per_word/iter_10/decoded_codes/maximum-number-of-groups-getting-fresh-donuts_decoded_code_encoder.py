from functools import cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        @cache
        def dp(remainder, *counts):
            counts = list(counts)
            max_happy = 0
            for i in range(batchSize):
                if counts[i] == 0:
                    continue
                counts[i] -= 1
                new_remainder = (remainder - i) % batchSize
                happy_groups = dp(new_remainder, *counts)
                if remainder == 0:
                    happy_groups += 1
                max_happy = max(max_happy, happy_groups)
                counts[i] += 1

            return max_happy

        return dp(0, *remainder_count)
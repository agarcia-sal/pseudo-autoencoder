from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize, groups):
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for g in groups:
            remainder_count[g % batchSize] += 1

        @lru_cache(None)
        def dp(remainder, *counts):
            counts = list(counts)
            max_happy = 0
            for i in range(batchSize):
                if counts[i] == 0:
                    continue
                counts[i] -= 1
                new_remainder = (remainder - i) % batchSize
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, *counts)
                else:
                    happy_groups = dp(new_remainder, *counts)
                if happy_groups > max_happy:
                    max_happy = happy_groups
                counts[i] += 1
            return max_happy

        return dp(0, *remainder_count)
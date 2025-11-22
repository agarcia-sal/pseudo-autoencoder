from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize, groups):
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        @lru_cache(None)
        def dp(remainder, *counts):
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

        return dp(0, *remainder_count)
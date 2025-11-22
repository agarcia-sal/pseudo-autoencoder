class Solution:
    def maxHappyGroups(self, batchSize, groups):
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(remainder, *remainder_count):
            remainder_count = list(remainder_count)
            max_happy = 0

            for i in range(batchSize):
                if remainder_count[i] == 0:
                    continue
                remainder_count[i] -= 1
                new_remainder = (remainder - i) % batchSize

                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, *remainder_count)
                else:
                    happy_groups = dp(new_remainder, *remainder_count)

                if happy_groups > max_happy:
                    max_happy = happy_groups

                remainder_count[i] += 1

            return max_happy

        return dp(0, *remainder_count)
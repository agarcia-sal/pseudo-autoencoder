from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        # Since groups with remainder 0 directly form happy groups
        initial_happy = remainder_count[0]
        remainder_count = remainder_count[1:]

        @lru_cache(None)
        def dp(remainder: int, counts: tuple[int, ...]) -> int:
            max_happy = 0
            counts_list = list(counts)
            for i, c in enumerate(counts_list):
                if c == 0:
                    continue
                counts_list[i] -= 1
                new_remainder = (remainder - (i + 1)) % batchSize
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, tuple(counts_list))
                else:
                    happy_groups = dp(new_remainder, tuple(counts_list))
                max_happy = max(max_happy, happy_groups)
                counts_list[i] += 1
            return max_happy

        return initial_happy + dp(0, tuple(remainder_count))
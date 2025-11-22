from functools import lru_cache
from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        remainder_count = [0] * batchSize
        for group in groups:
            remainder_count[group % batchSize] += 1

        # Convert remainder_count list to tuple except remainder_count[0],
        # since remainder_count[0] groups are already "happy" by themselves.
        # We'll include remainder_count[0] in dp state as it is.

        # The dp state will include:
        # - current remainder accumulation
        # - the counts of each remainder 1..batchSize-1
        #
        # Because remainder_count[0] groups don't affect state as they form happy groups immediately,
        # we can add them upfront to the final answer.

        # Precount groups with remainder 0 (always happy)
        initial_happy = remainder_count[0]

        # We only need to keep track of remainders from 1 to batchSize-1 for the DP state
        counts = tuple(remainder_count[1:])

        @lru_cache(None)
        def dp(remainder: int, counts_state: tuple) -> int:
            max_happy = 0
            counts_list = list(counts_state)
            for i in range(batchSize - 1):
                if counts_list[i] == 0:
                    continue
                counts_list[i] -= 1
                new_remainder = (remainder - (i + 1)) % batchSize
                # If remainder is zero before choosing this group,
                # picking this group forms a happy group because current group starts fresh.
                if remainder == 0:
                    happy_groups = 1 + dp(new_remainder, tuple(counts_list))
                else:
                    happy_groups = dp(new_remainder, tuple(counts_list))
                max_happy = max(max_happy, happy_groups)
                counts_list[i] += 1
            return max_happy

        return initial_happy + dp(0, counts)
from typing import Tuple

class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(index: int, slots: Tuple[int, ...]) -> int:
            if index == len(nums):
                return 0
            max_and_sum = 0
            slots_list = list(slots)
            for i in range(numSlots):
                if slots_list[i] < 2:
                    slots_list[i] += 1
                    and_sum = (nums[index] & (i + 1)) + dp(index + 1, tuple(slots_list))
                    if and_sum > max_and_sum:
                        max_and_sum = and_sum
                    slots_list[i] -= 1
            return max_and_sum

        initial_slots = (0,) * numSlots
        return dp(0, initial_slots)
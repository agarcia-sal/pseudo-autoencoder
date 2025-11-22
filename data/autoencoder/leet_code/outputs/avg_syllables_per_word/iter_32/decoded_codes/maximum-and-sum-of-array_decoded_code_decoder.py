from typing import List, Tuple
from functools import lru_cache

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        # dp function parameters:
        # index: current index in nums
        # slots: a tuple representing how many numbers are assigned to each slot (max 2 per slot)
        @lru_cache(None)
        def dp(index: int, slots: Tuple[int, ...]) -> int:
            if index == len(nums):
                return 0

            max_and_sum = 0
            slots_list = list(slots)

            for i in range(numSlots):
                if slots_list[i] < 2:
                    slots_list[i] += 1
                    current_and = (nums[index] & (i + 1)) + dp(index + 1, tuple(slots_list))
                    if current_and > max_and_sum:
                        max_and_sum = current_and
                    slots_list[i] -= 1

            return max_and_sum

        initial_slots = tuple(0 for _ in range(numSlots))
        return dp(0, initial_slots)
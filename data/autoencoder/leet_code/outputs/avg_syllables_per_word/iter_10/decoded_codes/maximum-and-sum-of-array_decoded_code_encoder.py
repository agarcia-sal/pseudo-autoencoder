from functools import cache

class Solution:
    def maximumANDSum(self, nums, numSlots):
        n = len(nums)

        @cache
        def dp(index, slots):
            if index == n:
                return 0

            max_and_sum = 0
            slots_list = list(slots)

            for i in range(len(slots_list)):
                if slots_list[i] < 2:
                    slots_list[i] += 1
                    current_sum = (nums[index] & (i + 1)) + dp(index + 1, tuple(slots_list))
                    if current_sum > max_and_sum:
                        max_and_sum = current_sum
                    slots_list[i] -= 1

            return max_and_sum

        initial_slots = (0,) * numSlots
        return dp(0, initial_slots)
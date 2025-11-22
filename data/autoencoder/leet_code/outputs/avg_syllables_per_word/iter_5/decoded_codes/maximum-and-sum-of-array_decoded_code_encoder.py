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
            for i in range(numSlots):
                if slots_list[i] < 2:
                    slots_list[i] += 1
                    and_sum = (nums[index] & (i + 1)) + dp(index + 1, tuple(slots_list))
                    if and_sum > max_and_sum:
                        max_and_sum = and_sum
                    slots_list[i] -= 1
            return max_and_sum

        return dp(0, (0,) * numSlots)
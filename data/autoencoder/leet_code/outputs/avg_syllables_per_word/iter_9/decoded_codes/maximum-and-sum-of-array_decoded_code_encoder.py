from functools import lru_cache

class Solution:
    def maximumANDSum(self, nums, numSlots):
        n = len(nums)

        @lru_cache(None)
        def dp(index, slots):
            if index == n:
                return 0

            max_and_sum = 0
            slots_list = list(slots)
            for i in range(numSlots):
                if slots_list[i] < 2:
                    slots_list[i] += 1
                    curr = (nums[index] & (i + 1)) + dp(index + 1, tuple(slots_list))
                    if curr > max_and_sum:
                        max_and_sum = curr
                    slots_list[i] -= 1
            return max_and_sum

        return dp(0, (0,) * numSlots)
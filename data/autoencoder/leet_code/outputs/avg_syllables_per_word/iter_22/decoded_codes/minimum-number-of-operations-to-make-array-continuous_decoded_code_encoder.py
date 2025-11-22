from bisect import bisect_left

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        unique_nums = sorted(set(nums))
        min_operations = n
        j = 0
        for i in range(len(unique_nums)):
            # Move j forward until unique_nums[j] >= unique_nums[i] + n
            while j < len(unique_nums) and unique_nums[j] < unique_nums[i] + n:
                j += 1
            current_window_size = j - i
            min_operations = min(min_operations, n - current_window_size)
        return min_operations
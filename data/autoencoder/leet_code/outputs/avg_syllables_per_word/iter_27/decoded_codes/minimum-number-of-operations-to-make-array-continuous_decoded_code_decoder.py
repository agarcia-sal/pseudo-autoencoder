from bisect import bisect_left

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        unique_nums = sorted(set(nums))
        min_operations = n
        j = 0
        for i in range(len(unique_nums)):
            # Using bisect_left to find the smallest index j >= current j
            # where unique_nums[j] >= unique_nums[i] + n
            # This avoids the linear while loop for efficiency.
            target = unique_nums[i] + n
            j = bisect_left(unique_nums, target, lo=j)
            min_operations = min(min_operations, n - (j - i))
        return min_operations
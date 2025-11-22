class Solution:
    def minOperations(self, nums):
        n = len(nums)
        unique_nums = sorted(set(nums))

        min_operations = n
        j = 0

        for i in range(len(unique_nums)):
            while j < len(unique_nums) and unique_nums[j] < unique_nums[i] + n:
                j += 1
            min_operations = min(min_operations, n - (j - i))

        return min_operations
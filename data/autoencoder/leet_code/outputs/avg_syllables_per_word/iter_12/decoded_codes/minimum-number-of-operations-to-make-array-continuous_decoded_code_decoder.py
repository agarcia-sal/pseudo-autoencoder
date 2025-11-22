class Solution:
    def minOperations(self, nums):
        n = len(nums)
        unique_nums = sorted(set(nums))
        min_operations = n
        j = 0
        for i in range(len(unique_nums)):
            while j < len(unique_nums) and unique_nums[j] < unique_nums[i] + n:
                j += 1
            current_operations = n - (j - i)
            if current_operations < min_operations:
                min_operations = current_operations
        return min_operations
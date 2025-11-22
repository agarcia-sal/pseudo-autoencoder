class Solution:
    def minOperations(self, nums):
        n = len(nums)
        unique_nums = sorted(set(nums))
        min_operations = n
        j = 0
        length = len(unique_nums)
        for i in range(length):
            while j < length and unique_nums[j] < unique_nums[i] + n:
                j += 1
            min_operations = min(min_operations, n - (j - i))
        return min_operations
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for index in range(n):
            while 1 <= nums[index] <= n and nums[nums[index] - 1] != nums[index]:
                correct_index = nums[index] - 1
                nums[index], nums[correct_index] = nums[correct_index], nums[index]
        for index in range(n):
            if nums[index] != index + 1:
                return index + 1
        return n + 1
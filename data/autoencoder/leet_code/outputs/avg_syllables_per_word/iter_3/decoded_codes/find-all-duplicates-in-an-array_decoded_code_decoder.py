class Solution:
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i], nums[temp - 1] = nums[temp - 1], temp
        return [nums[i] for i in range(len(nums)) if nums[i] != i + 1]
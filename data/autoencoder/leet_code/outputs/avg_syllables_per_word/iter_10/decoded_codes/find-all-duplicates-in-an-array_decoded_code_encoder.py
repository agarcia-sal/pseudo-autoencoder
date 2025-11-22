class Solution:
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i], nums[temp - 1] = nums[temp - 1], temp
        duplicates_list = [v for i, v in enumerate(nums) if v != i + 1]
        return duplicates_list
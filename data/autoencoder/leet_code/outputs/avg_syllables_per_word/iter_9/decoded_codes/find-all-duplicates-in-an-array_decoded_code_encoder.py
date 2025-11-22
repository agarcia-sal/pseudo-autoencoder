class Solution:
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i], nums[tmp - 1] = nums[tmp - 1], nums[i]
        result = [v for i, v in enumerate(nums) if v != i + 1]
        return result
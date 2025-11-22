class Solution:
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        result_list = []
        for index, value in enumerate(nums):
            if value != index + 1:
                result_list.append(value)
        return result_list
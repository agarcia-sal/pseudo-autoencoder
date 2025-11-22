class Solution:
    def findDuplicates(self, nums):
        for index in range(len(nums)):
            while nums[index] != nums[nums[index] - 1]:
                tmp = nums[index]
                nums[index] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        result_list = []
        for element_index, element_value in enumerate(nums):
            if element_value != element_index + 1:
                result_list.append(element_value)
        return result_list
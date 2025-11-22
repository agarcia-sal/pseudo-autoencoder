class Solution:
    def nextPermutation(self, nums):
        index_i = len(nums) - 2
        while index_i >= 0 and nums[index_i] >= nums[index_i + 1]:
            index_i -= 1

        if index_i >= 0:
            index_j = len(nums) - 1
            while nums[index_j] <= nums[index_i]:
                index_j -= 1
            nums[index_i], nums[index_j] = nums[index_j], nums[index_i]

        nums[index_i + 1 :] = reversed(nums[index_i + 1 :])
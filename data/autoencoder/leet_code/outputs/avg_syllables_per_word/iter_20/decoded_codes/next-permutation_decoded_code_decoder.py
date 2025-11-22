class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left_index = i + 1
        right_index = len(nums) - 1
        while left_index < right_index:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index += 1
            right_index -= 1
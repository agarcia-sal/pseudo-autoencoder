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
        sublist = nums[i + 1:]
        reversed_sublist = sublist[::-1]
        for index in range(len(reversed_sublist)):
            nums[i + 1 + index] = reversed_sublist[index]
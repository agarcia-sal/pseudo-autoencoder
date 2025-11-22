class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        start = -1
        end = -2
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if start == -1:
                    start = i
                end = i
        return end - start + 1
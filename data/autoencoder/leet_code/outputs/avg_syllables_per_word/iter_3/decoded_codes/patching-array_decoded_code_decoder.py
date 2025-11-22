class Solution:
    def minPatches(self, nums, n):
        missing, patches, i = 1, 0, 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                patches += 1
        return patches
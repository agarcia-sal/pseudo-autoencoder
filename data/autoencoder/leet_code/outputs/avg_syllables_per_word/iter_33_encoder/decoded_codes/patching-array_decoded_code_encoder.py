class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        missing = 1
        patches = 0
        i = 0
        length = len(nums)

        while missing <= n:
            if i < length and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                patches += 1

        return patches
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to the next lexicographical permutation.
        If such arrangement is not possible, it must rearrange to the lowest possible order (sorted ascending).
        """
        i = len(nums) - 2
        # Find the first index 'i' from the end such that nums[i] < nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            # Find the first index 'j' from the end such that nums[j] > nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse elements from i+1 till end to get the next smallest lexicographic permutation
        start, end = i + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
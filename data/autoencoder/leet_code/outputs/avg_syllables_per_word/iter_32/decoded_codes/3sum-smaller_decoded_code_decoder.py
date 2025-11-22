from typing import List

class Solution:  
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    # If nums[i] + nums[left] + nums[right] < target,
                    # then all sums from left+1 to right will also be smaller, because the array is sorted.
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count
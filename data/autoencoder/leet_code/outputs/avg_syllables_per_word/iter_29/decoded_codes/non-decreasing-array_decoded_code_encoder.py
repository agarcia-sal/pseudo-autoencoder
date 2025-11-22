from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modification_made = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modification_made:
                    return False
                modification_made = True
                if i < 2 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True
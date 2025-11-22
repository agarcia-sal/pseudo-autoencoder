from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return f"{nums[0]} DIVIDED BY {nums[1]}"
        else:
            return f"{nums[0]} DIVIDED BY ({' DIVIDED BY '.join(map(str, nums[1:]))})"
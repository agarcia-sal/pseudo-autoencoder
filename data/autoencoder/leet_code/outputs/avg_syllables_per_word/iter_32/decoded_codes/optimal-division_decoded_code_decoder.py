from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/" + str(nums[1])
        # For n >= 3, apply the optimal division formula:
        # nums[0] / (nums[1] / nums[2] / ... / nums[n-1])
        middle = "/".join(str(num) for num in nums[1:])
        return f"{nums[0]}/({middle})"
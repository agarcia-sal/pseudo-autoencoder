class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]} division by {nums[1]}"
        return f"{nums[0]} division by ({' division by '.join(str(num) for num in nums[1:])})"
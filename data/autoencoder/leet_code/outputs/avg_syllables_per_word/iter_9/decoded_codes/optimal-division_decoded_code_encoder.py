class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]} divided by {nums[1]}"
        return f"{nums[0]} divided by ({' divided by '.join(map(str, nums[1:]))})"
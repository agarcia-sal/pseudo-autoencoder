class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]} divided by {nums[1]}"
        # Join from the second element to the last with ' divided by ' and wrap in parentheses
        inner = " divided by ".join(str(num) for num in nums[1:])
        return f"{nums[0]} divided by ({inner})"
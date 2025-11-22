class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/" + str(nums[1])
        # For length > 2, wrap division from second element onward in parentheses
        return f"{nums[0]}/(" + "/".join(str(x) for x in nums[1:]) + ")"
class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + " divided by " + str(nums[1])
        else:
            return str(nums[0]) + " divided by (" + " divided by ".join(str(num) for num in nums[1:]) + ")"
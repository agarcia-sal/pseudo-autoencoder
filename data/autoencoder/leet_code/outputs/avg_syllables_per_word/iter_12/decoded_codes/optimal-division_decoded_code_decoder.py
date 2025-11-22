class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/" + str(nums[1])
        inner_expression = str(nums[1])
        for num in nums[2:]:
            inner_expression += "/" + str(num)
        return f"{nums[0]}/({inner_expression})"
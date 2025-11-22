class Solution:
    def checkPossibility(self, nums):
        modified = False
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                if modified:
                    return False
                modified = True
                if index < 2 or nums[index] >= nums[index - 2]:
                    nums[index - 1] = nums[index]
                else:
                    nums[index] = nums[index - 1]
        return True
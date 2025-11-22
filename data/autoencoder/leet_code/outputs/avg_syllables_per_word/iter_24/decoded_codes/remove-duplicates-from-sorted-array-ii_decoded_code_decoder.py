class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        write_index = 2 if len(nums) > 1 else len(nums)
        for i in range(2, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
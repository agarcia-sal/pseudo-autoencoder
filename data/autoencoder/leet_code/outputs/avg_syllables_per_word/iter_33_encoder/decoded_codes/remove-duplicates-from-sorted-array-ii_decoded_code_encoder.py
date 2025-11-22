class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        write_index = min(2, len(nums))
        for i in range(write_index, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
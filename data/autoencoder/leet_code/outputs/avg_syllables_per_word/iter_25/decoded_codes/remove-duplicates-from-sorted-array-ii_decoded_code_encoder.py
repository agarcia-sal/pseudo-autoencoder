from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write_index = 0
        limit = min(2, len(nums))
        for i in range(limit):
            nums[write_index] = nums[i]
            write_index += 1
        for i in range(2, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        write_index = 0

        for i in range(min(2, len(nums))):
            nums[write_index] = nums[i]
            write_index += 1

        for i in range(2, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
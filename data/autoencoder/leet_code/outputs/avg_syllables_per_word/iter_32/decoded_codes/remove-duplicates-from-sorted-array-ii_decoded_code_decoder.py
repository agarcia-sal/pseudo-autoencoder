from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write_index = 0
        # Copy the first two elements as is (or less if nums length < 2)
        for i in range(min(2, len(nums))):
            nums[write_index] = nums[i]
            write_index += 1
        # From the third element onwards, only copy if nums[i] != nums[write_index - 2]
        for i in range(2, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
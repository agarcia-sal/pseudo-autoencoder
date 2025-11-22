from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write_index = 0

        # Copy up to two elements directly
        for i in range(min(2, len(nums))):
            nums[write_index] = nums[i]
            write_index += 1

        # From the third element onwards, only copy if different from the element two positions behind
        for i in range(2, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
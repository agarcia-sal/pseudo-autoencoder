class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0

        write_index = 0

        # Copy first two elements as is
        for i in range(min(2, len(nums))):
            nums[write_index] = nums[i]
            write_index += 1

        # From the third element onward, keep element only if it differs from
        # the element at write_index-2, allowing at most two duplicates
        for i in range(2, len(nums)):
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
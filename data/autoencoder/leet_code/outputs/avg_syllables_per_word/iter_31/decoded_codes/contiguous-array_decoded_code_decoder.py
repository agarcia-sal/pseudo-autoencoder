from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum_index = {0: -1}
        max_length = 0
        count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in prefix_sum_index:
                subarray_length = i - prefix_sum_index[count]
                if subarray_length > max_length:
                    max_length = subarray_length
            else:
                prefix_sum_index[count] = i

        return max_length
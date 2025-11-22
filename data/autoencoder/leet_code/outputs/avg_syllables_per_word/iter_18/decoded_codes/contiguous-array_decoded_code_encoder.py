from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum_index = {0: -1}
        max_length = 0
        count = 0
        for index, element in enumerate(nums):
            if element == 1:
                count += 1
            else:
                count -= 1
            if count in prefix_sum_index:
                max_length = max(max_length, index - prefix_sum_index[count])
            else:
                prefix_sum_index[count] = index
        return max_length
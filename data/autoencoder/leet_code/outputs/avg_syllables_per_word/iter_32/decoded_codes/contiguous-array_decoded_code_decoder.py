from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum_index = {0: -1}  # Maps count to earliest index
        max_length = 0
        count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in prefix_sum_index:
                # Calculate the length of subarray with equal number of 0s and 1s
                current_length = i - prefix_sum_index[count]
                if current_length > max_length:
                    max_length = current_length
            else:
                prefix_sum_index[count] = i

        return max_length
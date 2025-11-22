from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(max_value: int) -> int:
            count = 0
            current_length = 0
            for num in nums:
                if num <= max_value:
                    current_length += 1
                    count += current_length
                else:
                    current_length = 0
            return count

        result_lower_bound = count(right)
        result_upper_bound = count(left - 1)
        return result_lower_bound - result_upper_bound
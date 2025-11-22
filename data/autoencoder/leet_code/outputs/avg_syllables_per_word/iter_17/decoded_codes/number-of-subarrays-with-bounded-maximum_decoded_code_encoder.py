from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(max_value: int) -> int:
            total_count = 0
            current_length = 0
            for num in nums:
                if num <= max_value:
                    current_length += 1
                    total_count += current_length
                else:
                    current_length = 0
            return total_count

        return count(right) - count(left - 1)
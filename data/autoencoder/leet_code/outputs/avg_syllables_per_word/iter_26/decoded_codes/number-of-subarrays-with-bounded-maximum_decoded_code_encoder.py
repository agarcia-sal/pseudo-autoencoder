from typing import List

class Solution:
    def numSubarrayBoundedMax(self, list_of_numbers: List[int], left_boundary: int, right_boundary: int) -> int:
        def count(max_value: int) -> int:
            total_count = 0
            current_consecutive_length = 0
            for number in list_of_numbers:
                if number <= max_value:
                    current_consecutive_length += 1
                    total_count += current_consecutive_length
                else:
                    current_consecutive_length = 0
            return total_count

        return count(right_boundary) - count(left_boundary - 1)
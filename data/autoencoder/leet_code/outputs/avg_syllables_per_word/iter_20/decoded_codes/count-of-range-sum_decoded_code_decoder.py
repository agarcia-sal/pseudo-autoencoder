from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sums = [0]
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            left = current_sum - upper
            right = current_sum - lower

            left_idx = bisect_left(prefix_sums, left)
            right_idx = bisect_right(prefix_sums, right)

            count += right_idx - left_idx

            # Insert current_sum keeping prefix_sums sorted
            insert_pos = bisect_right(prefix_sums, current_sum)
            prefix_sums.insert(insert_pos, current_sum)

        return count
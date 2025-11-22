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

            count += bisect_right(prefix_sums, right) - bisect_left(prefix_sums, left)
            # Insert current_sum maintaining sorted order
            prefix_sums.insert(bisect_right(prefix_sums, current_sum), current_sum)

        return count
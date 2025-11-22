from bisect import bisect_left, bisect_right, insort
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

            # Number of prefix sums <= right
            right_count = bisect_right(prefix_sums, right)
            # Number of prefix sums < left
            left_count = bisect_left(prefix_sums, left)

            count += right_count - left_count
            insort(prefix_sums, current_sum)

        return count
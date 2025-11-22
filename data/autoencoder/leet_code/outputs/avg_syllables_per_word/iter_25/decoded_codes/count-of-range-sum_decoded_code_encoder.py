import bisect
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
            # Count the number of prefix sums within [left, right]
            count += bisect.bisect_right(prefix_sums, right) - bisect.bisect_left(prefix_sums, left)
            bisect.insort(prefix_sums, current_sum)
        return count
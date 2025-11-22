from bisect import bisect_left, bisect_right

class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix_sums = [0]
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            left = current_sum - upper
            right = current_sum - lower
            count += bisect_right(prefix_sums, right) - bisect_left(prefix_sums, left)
            # Insert current_sum in sorted order
            idx = bisect_right(prefix_sums, current_sum)
            prefix_sums.insert(idx, current_sum)

        return count
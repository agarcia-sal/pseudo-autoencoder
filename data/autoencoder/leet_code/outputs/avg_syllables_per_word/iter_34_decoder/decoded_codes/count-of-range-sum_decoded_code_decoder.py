import bisect

class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix_sums = [0]
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            left = current_sum - upper
            right = current_sum - lower

            left_idx = bisect.bisect_left(prefix_sums, left)
            right_idx = bisect.bisect_right(prefix_sums, right)

            count += right_idx - left_idx

            bisect.insort(prefix_sums, current_sum)

        return count
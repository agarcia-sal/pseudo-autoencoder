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

            # number of prefix sums in [left, right] is:
            # position to the right of 'right' - position to the left of 'left'
            count += bisect.bisect_right(prefix_sums, right) - bisect.bisect_left(prefix_sums, left)
            bisect.insort(prefix_sums, current_sum)

        return count
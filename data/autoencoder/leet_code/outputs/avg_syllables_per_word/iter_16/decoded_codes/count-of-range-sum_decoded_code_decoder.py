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

            left_index = bisect.bisect_left(prefix_sums, left)
            right_index = bisect.bisect_right(prefix_sums, right)

            count += right_index - left_index
            bisect.insort(prefix_sums, current_sum)

        return count
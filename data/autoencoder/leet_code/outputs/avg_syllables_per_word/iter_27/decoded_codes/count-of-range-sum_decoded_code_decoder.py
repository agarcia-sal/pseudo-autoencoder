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
            left_idx = bisect_left(prefix_sums, left)
            right_idx = bisect_right(prefix_sums, right)
            count += right_idx - left_idx
            # Insert current_sum into prefix_sums maintaining sorted order
            insert_idx = bisect_left(prefix_sums, current_sum)
            prefix_sums.insert(insert_idx, current_sum)
        return count
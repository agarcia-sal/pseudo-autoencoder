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

            # Count how many prefix sums fall in the range [left, right]
            left_index = bisect_left(prefix_sums, left)
            right_index = bisect_right(prefix_sums, right)
            count += right_index - left_index

            # Insert current_sum into prefix_sums to maintain sorted order
            insert_pos = bisect_right(prefix_sums, current_sum)
            prefix_sums.insert(insert_pos, current_sum)

        return count
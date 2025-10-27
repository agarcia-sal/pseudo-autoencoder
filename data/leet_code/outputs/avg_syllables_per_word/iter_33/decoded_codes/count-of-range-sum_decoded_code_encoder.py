from bisect import bisect_left, bisect_right, insort

class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix_sums = [0]
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            left = current_sum - upper
            right = current_sum - lower

            # Count how many prefix sums are <= right
            number_of_elements_to_right = bisect_right(prefix_sums, right)
            # Count how many prefix sums are < left
            number_of_elements_to_left = bisect_left(prefix_sums, left)

            count += number_of_elements_to_right - number_of_elements_to_left

            insort(prefix_sums, current_sum)

        return count
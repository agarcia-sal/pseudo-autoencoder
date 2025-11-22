from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        total_length = len(nums)
        list_of_sums = [0] * (total_length - k + 1)

        # Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        list_of_sums[0] = current_sum

        # Calculate sums of windows of size k starting from each index
        for i in range(1, total_length - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            list_of_sums[i] = current_sum

        list_left = [0] * (total_length - k + 1)
        list_right = [total_length - k] * (total_length - k + 1)

        max_sum_position = 0
        for i in range(total_length - k + 1):
            if list_of_sums[i] > list_of_sums[max_sum_position]:
                max_sum_position = i
            list_left[i] = max_sum_position

        max_sum_position = total_length - k
        for i in range(total_length - k, -1, -1):
            if list_of_sums[i] >= list_of_sums[max_sum_position]:
                max_sum_position = i
            list_right[i] = max_sum_position

        max_total_sum = 0
        result_indices = [0, 0, 0]
        for middle_index in range(k, total_length - 2 * k + 1):
            left_index = list_left[middle_index - k]
            right_index = list_right[middle_index + k]
            total_of_three = list_of_sums[left_index] + list_of_sums[middle_index] + list_of_sums[right_index]
            if total_of_three > max_total_sum:
                max_total_sum = total_of_three
                result_indices = [left_index, middle_index, right_index]

        return result_indices
class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        cumulative_sum_index = {0: -1}
        cumulative_sum = 0
        max_length = 0

        for index, num in enumerate(nums):
            cumulative_sum += num

            diff = cumulative_sum - k
            if diff in cumulative_sum_index:
                max_length = max(max_length, index - cumulative_sum_index[diff])

            if cumulative_sum not in cumulative_sum_index:
                cumulative_sum_index[cumulative_sum] = index

        return max_length
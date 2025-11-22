class Solution:
    def maxSubArrayLen(self, nums, k):
        cumulative_sum_index = {0: -1}
        cumulative_sum = 0
        max_length = 0
        for i, num in enumerate(nums):
            cumulative_sum += num
            if (cumulative_sum - k) in cumulative_sum_index:
                candidate_length = i - cumulative_sum_index[cumulative_sum - k]
                if candidate_length > max_length:
                    max_length = candidate_length
            if cumulative_sum not in cumulative_sum_index:
                cumulative_sum_index[cumulative_sum] = i
        return max_length
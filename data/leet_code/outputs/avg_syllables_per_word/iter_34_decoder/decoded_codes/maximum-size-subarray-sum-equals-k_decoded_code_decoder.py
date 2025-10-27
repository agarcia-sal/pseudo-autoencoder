class Solution:
    def maxSubArrayLen(self, nums, k):
        cum_sum_index = {0: -1}
        cum_sum = 0
        max_length = 0
        for i, num in enumerate(nums):
            cum_sum += num
            if (cum_sum - k) in cum_sum_index:
                candidate_length = i - cum_sum_index[cum_sum - k]
                if candidate_length > max_length:
                    max_length = candidate_length
            if cum_sum not in cum_sum_index:
                cum_sum_index[cum_sum] = i
        return max_length
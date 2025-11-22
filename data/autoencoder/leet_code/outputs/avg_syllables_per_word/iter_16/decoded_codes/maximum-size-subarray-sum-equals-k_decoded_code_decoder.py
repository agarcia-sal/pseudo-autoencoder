class Solution:
    def maxSubArrayLen(self, nums, k):
        cum_sum_index = {0: -1}
        cum_sum = 0
        max_length = 0

        for index, num in enumerate(nums):
            cum_sum += num
            if (cum_sum - k) in cum_sum_index:
                diff_index = cum_sum_index[cum_sum - k]
                max_length = max(max_length, index - diff_index)
            if cum_sum not in cum_sum_index:
                cum_sum_index[cum_sum] = index

        return max_length
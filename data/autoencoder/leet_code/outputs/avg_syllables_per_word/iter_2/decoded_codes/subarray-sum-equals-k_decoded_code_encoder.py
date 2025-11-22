class Solution:
    def subarraySum(self, nums, k):
        cumulative_sum_freq = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            if current_sum - k in cumulative_sum_freq:
                count += cumulative_sum_freq[current_sum - k]
            if current_sum in cumulative_sum_freq:
                cumulative_sum_freq[current_sum] += 1
            else:
                cumulative_sum_freq[current_sum] = 1
        return count
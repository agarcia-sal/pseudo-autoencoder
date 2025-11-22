class Solution:
    def subarraySum(self, nums, k):
        cumulative_sum_freq = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            if current_sum - k in cumulative_sum_freq:
                count += cumulative_sum_freq[current_sum - k]
            cumulative_sum_freq[current_sum] = cumulative_sum_freq.get(current_sum, 0) + 1

        return count
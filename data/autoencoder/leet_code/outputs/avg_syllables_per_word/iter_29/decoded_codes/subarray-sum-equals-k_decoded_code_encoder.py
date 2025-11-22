from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        dictionary_of_cumulative_sum_frequencies = defaultdict(int, {0: 1})
        accumulated_sum = 0
        count_of_subarrays = 0
        for number in nums:
            accumulated_sum += number
            if (accumulated_sum - k) in dictionary_of_cumulative_sum_frequencies:
                count_of_subarrays += dictionary_of_cumulative_sum_frequencies[accumulated_sum - k]
            dictionary_of_cumulative_sum_frequencies[accumulated_sum] += 1
        return count_of_subarrays
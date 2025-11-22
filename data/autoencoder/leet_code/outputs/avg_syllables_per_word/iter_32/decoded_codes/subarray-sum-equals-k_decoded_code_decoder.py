from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum_freq = defaultdict(int)
        cumulative_sum_freq[0] = 1  # Base case: zero cumulative sum occurs once
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            if (current_sum - k) in cumulative_sum_freq:
                count += cumulative_sum_freq[current_sum - k]
            cumulative_sum_freq[current_sum] += 1

        return count
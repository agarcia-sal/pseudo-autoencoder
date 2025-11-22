from collections import Counter
from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums) if nums else 0
        count = Counter(nums)

        prefix_sum = [0] * (max_num + 1)
        # Populate prefix sums with frequencies
        for num, freq in count.items():
            prefix_sum[num] += freq

        # Build prefix sums for quick range queries
        for i in range(1, max_num + 1):
            prefix_sum[i] += prefix_sum[i - 1]

        result = 0
        for num, freq in count.items():
            max_multiple = max_num // num
            for multiple in range(1, max_multiple + 1):
                start = num * multiple
                end = min(num * (multiple + 1) - 1, max_num)
                multiples_count = prefix_sum[end] - prefix_sum[start - 1] if start > 0 else prefix_sum[end]
                # Add contribution for this multiple
                result += multiples_count * multiple * freq
                result %= MOD

        return result
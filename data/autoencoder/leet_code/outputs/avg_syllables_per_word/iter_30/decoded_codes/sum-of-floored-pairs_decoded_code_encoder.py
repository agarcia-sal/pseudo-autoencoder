from collections import Counter
from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)
        count = Counter(nums)

        prefix_sum = [0] * (max_num + 1)
        for num, c in count.items():
            prefix_sum[num] += c

        for i in range(1, max_num + 1):
            prefix_sum[i] += prefix_sum[i - 1]

        result = 0
        for num, c in count.items():
            max_multiple = max_num // num
            for multiple in range(1, max_multiple + 1):
                start = num * multiple
                end = min(num * multiple + multiple - 1, max_num)
                multiples_count = prefix_sum[end] - prefix_sum[start - 1]
                result += multiples_count * multiple * c
                result %= MOD

        return result
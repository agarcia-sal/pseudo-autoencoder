from collections import Counter

class Solution:
    def sumOfFlooredPairs(self, nums):
        MOD = 10**9 + 7
        max_num = max(nums) if nums else 0
        count = Counter(nums)
        prefix_sum = [0] * (max_num + 1)

        for num, freq in count.items():
            prefix_sum[num] += freq

        for i in range(1, max_num + 1):
            prefix_sum[i] += prefix_sum[i - 1]

        result = 0

        for num, freq in count.items():
            multiple = 1
            while multiple * num <= max_num:
                start = multiple * num
                end = min(multiple * num + num - 1, max_num)
                multiples_count = prefix_sum[end] - prefix_sum[start - 1]  # inclusive range [start, end]
                result += multiples_count * multiple * freq
                result %= MOD
                multiple += 1

        return result
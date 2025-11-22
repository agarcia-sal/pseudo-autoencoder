from collections import Counter

class Solution:
    def sumOfFlooredPairs(self, nums):
        MOD = 10**9 + 7
        max_num = max(nums)
        count = Counter(nums)
        prefix_sum = [0] * (max_num + 1)

        # Fill prefix_sum with counts
        for num in count:
            prefix_sum[num] += count[num]

        # Build prefix sums
        for i in range(1, max_num + 1):
            prefix_sum[i] += prefix_sum[i - 1]

        result = 0

        for num in count:
            c = count[num]
            multiple = 1
            while multiple * num <= max_num:
                start = multiple * num
                end = min((multiple + 1) * num - 1, max_num)
                multiples_count = prefix_sum[end] - prefix_sum[start - 1] if start > 0 else prefix_sum[end]
                result += multiples_count * multiple * c
                result %= MOD
                multiple += 1

        return result % MOD
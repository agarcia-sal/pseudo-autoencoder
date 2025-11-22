class Solution:
    def sumOfFlooredPairs(self, nums):
        MOD = 10**9 + 7
        max_num = max(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        prefix_sum = [0] * (max_num + 1)
        for num in count:
            prefix_sum[num] += count[num]

        for i in range(1, max_num + 1):
            prefix_sum[i] += prefix_sum[i - 1]

        result = 0
        for num in count:
            max_multiple = max_num // num
            for multiple in range(1, max_multiple + 1):
                start = num * multiple
                end = min(num * (multiple + 1) - 1, max_num)
                multiples_count = prefix_sum[end] - prefix_sum[start - 1]
                result += multiples_count * multiple * count[num]
                result %= MOD

        return result
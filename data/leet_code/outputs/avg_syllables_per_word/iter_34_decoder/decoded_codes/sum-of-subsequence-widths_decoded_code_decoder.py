class Solution:
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        total_sum = 0
        power = [1] * n

        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        for i in range(n):
            total_sum += nums[i] * (power[i] - power[n - i - 1])
            total_sum %= MOD

        return total_sum
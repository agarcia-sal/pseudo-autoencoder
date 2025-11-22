class Solution:
    def sumSubseqWidths(self, nums):
        MOD = 1000000007
        nums.sort()
        n = len(nums)
        total_sum = 0
        power = [1] * n

        for i in range(1, n):
            power[i] = (power[i-1] * 2) % MOD

        for i in range(n):
            contribution = nums[i] * (power[i] - power[n - i - 1])
            total_sum = (total_sum + contribution) % MOD

        return total_sum
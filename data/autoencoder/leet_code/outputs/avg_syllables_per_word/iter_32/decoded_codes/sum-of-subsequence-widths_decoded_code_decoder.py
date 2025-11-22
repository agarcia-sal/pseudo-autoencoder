from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        power = [1] * n

        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        total_sum = 0
        for i in range(n):
            total_sum += nums[i] * power[i] - nums[i] * power[n - i - 1]
            total_sum %= MOD

        return total_sum
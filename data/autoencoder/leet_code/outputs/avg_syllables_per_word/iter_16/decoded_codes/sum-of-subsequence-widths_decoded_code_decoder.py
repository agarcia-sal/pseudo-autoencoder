class Solution:
    def sumSubseqWidths(self, nums):
        MODULO = 10**9 + 7
        nums.sort()
        n = len(nums)
        total_sum = 0
        power = [1] * n

        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MODULO

        for i in range(n):
            increment_value = nums[i] * (power[i] - power[n - i - 1]) % MODULO
            total_sum = (total_sum + increment_value) % MODULO

        return total_sum
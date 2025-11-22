class Solution:
    def sumSubseqWidths(self, nums):
        MODULO = 10**9 + 7
        nums.sort()
        n = len(nums)
        total_sum = 0
        power = [1] * n

        for index in range(1, n):
            power[index] = (power[index - 1] * 2) % MODULO

        for index in range(n):
            increment_value = nums[index] * (power[index] - power[n - index - 1])
            total_sum = (total_sum + increment_value) % MODULO

        return total_sum
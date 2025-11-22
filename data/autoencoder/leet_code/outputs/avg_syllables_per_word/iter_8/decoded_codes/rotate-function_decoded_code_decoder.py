class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        total_sum = sum(nums)
        current_sum = sum(i * nums[i] for i in range(n))

        max_value = current_sum

        for k in range(1, n):
            current_sum = current_sum + total_sum - n * nums[n - k]
            if current_sum > max_value:
                max_value = current_sum

        return max_value
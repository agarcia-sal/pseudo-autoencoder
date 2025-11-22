from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                count_at_j = dp[j][d]
                dp[i][d] += count_at_j + 1
                total_count += count_at_j
        return total_count
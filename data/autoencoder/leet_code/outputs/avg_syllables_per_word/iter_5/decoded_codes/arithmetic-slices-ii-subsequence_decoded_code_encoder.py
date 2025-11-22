class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0

        dp = [{} for _ in range(n)]
        total_count = 0

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                count = dp[j].get(d, 0)
                dp[i][d] = dp[i].get(d, 0) + count + 1
                total_count += count

        return total_count
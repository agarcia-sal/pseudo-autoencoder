class Solution:
    def canPartition(self, nums):
        total_sum = 0
        for number in nums:
            total_sum += number

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        self.n = len(nums)
        self.initialize_dp(target)

        for num in nums:
            for i in range(target, num - 1, -1):
                self.dp[i] = self.dp[i] or self.dp[i - num]

        return self.dp[target]

    def initialize_dp(self, target):
        self.dp = [False] * (target + 1)
        self.dp[0] = True
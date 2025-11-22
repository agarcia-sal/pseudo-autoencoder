from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0

        dp = self.create_list_of_defaultdicts(n)
        total_count = 0

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                if d in dp[j]:
                    dp[i][d] += dp[j][d] + 1
                    total_count += dp[j][d]
                else:
                    dp[i][d] += 1

        return total_count

    def create_list_of_defaultdicts(self, n):
        dp_list = []
        for _ in range(n):
            dp_list.append(defaultdict(int))
        return dp_list
class Solution:
    def canPartition(self, list_of_numbers):
        total_sum = sum(list_of_numbers)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        n = len(list_of_numbers)
        dp = [False] * (target + 1)
        dp[0] = True
        for number in list_of_numbers:
            for index in range(target, number - 1, -1):
                dp[index] = dp[index] or dp[index - number]
        return dp[target]
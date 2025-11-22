class Solution:
    def coinChange(self, list_of_coins, target_amount):
        dp = [target_amount + 1] * (target_amount + 1)
        dp[0] = 0

        for current_amount in range(1, target_amount + 1):
            for coin in list_of_coins:
                if current_amount - coin >= 0:
                    dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

        return dp[target_amount] if dp[target_amount] != target_amount + 1 else -1
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with amount+1 (an impossible high number of coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Zero coins needed to make amount zero

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            # Take one stone
            dp[i] = stoneValue[i] - dp[i + 1]

            # Take two stones if possible
            if i + 2 <= n:
                take_two = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                if take_two > dp[i]:
                    dp[i] = take_two

            # Take three stones if possible
            if i + 3 <= n:
                take_three = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                if take_three > dp[i]:
                    dp[i] = take_three

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
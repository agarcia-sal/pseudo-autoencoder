from typing import List

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MODULO = 10**9 + 7
        dp = [0, 0, 0]
        for num in nums:
            if num == 0:
                dp[0] = (2 * dp[0] + 1) % MODULO
            elif num == 1:
                dp[1] = (2 * dp[1] + dp[0]) % MODULO
            elif num == 2:
                dp[2] = (2 * dp[2] + dp[1]) % MODULO
        return dp[2]
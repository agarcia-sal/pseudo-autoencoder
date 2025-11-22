from typing import List

class Solution:
    def maxA(self, n: int) -> int:
        if n <= 3:
            return n

        dp: List[int] = [0] * (n + 1)
        for i in range(1, 4):
            dp[i] = i

        for i in range(4, n + 1):
            for j in range(i - 3, 0, -1):
                # max between current dp[i] and dp[j] * (i - j - 1),
                # where (i-j-1) represents the number of Ctrl-V operations after Ctrl-A and Ctrl-C at step j+1 and j+2
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[n]
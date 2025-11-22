class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # number of BSTs with j-1 nodes on the left and i-j nodes on the right
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]
class Solution:
    def superEggDrop(self, k, n):
        dp = [0] * (k + 1)
        moves = 0
        while dp[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                dp[eggs] = 1 + dp[eggs - 1] + dp[eggs]
        return moves
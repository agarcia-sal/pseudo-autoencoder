class Solution:
    def countSpecialSubsequences(self, list_of_numbers):
        MODULO = 10**9 + 7
        dp = [0, 0, 0]

        for number in list_of_numbers:
            if number == 0:
                dp[0] = (2 * dp[0] + 1) % MODULO
            elif number == 1:
                dp[1] = (2 * dp[1] + dp[0]) % MODULO
            elif number == 2:
                dp[2] = (2 * dp[2] + dp[1]) % MODULO

        return dp[2]
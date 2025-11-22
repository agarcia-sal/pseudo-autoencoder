class Solution:
    def numDecodings(self, string_input: str) -> int:
        if not string_input or string_input[0] == '0':
            return 0

        n = len(string_input)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if string_input[i - 1] != '0':
                dp[i] += dp[i - 1]

            two_digit = int(string_input[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
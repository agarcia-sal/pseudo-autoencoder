class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MODULO = 10**9 + 7
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        last_occurrence = {}

        for i in range(1, length + 1):
            current_char = s[i - 1]
            dp[i] = (dp[i - 1] * 2) % MODULO
            if current_char in last_occurrence:
                dp[i] = (dp[i] - dp[last_occurrence[current_char] - 1] + MODULO) % MODULO
            last_occurrence[current_char] = i

        return (dp[length] - 1) % MODULO
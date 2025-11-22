class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        def ways_to_decode_single(ch: str) -> int:
            if ch == '*':
                return 9
            if ch == '0':
                return 0
            return 1

        def ways_to_decode_pair(ch1: str, ch2: str) -> int:
            if ch1 == '*' and ch2 == '*':
                return 15
            if ch1 == '*':
                return 2 if ch2 <= '6' else 1
            if ch2 == '*':
                if ch1 == '1':
                    return 9
                if ch1 == '2':
                    return 6
                return 0
            num = int(ch1 + ch2)
            return 1 if 10 <= num <= 26 else 0

        for i in range(1, n + 1):
            dp[i] = (dp[i] + dp[i - 1] * ways_to_decode_single(s[i - 1])) % MOD
            if i > 1:
                dp[i] = (dp[i] + dp[i - 2] * ways_to_decode_pair(s[i - 2], s[i - 1])) % MOD

        return dp[n]
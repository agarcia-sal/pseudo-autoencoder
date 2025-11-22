class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        def ways_to_decode_single(char: str) -> int:
            if char == '*':
                return 9
            elif char == '0':
                return 0
            else:
                return 1

        def ways_to_decode_pair(char1: str, char2: str) -> int:
            if char1 == '*' and char2 == '*':
                return 15  # 11-19 and 21-26
            elif char1 == '*':
                if '0' <= char2 <= '6':
                    return 2  # *0-*6 can be 10-16 or 20-26
                else:
                    return 1  # *7-*9 can be 17-19 only
            elif char2 == '*':
                if char1 == '1':
                    return 9  # 11-19
                elif char1 == '2':
                    return 6  # 21-26
                else:
                    return 0
            else:
                num = int(char1 + char2)
                if 10 <= num <= 26:
                    return 1
                else:
                    return 0

        for i in range(1, n + 1):
            dp[i] = (dp[i] + dp[i - 1] * ways_to_decode_single(s[i - 1])) % MOD
            if i > 1:
                dp[i] = (dp[i] + dp[i - 2] * ways_to_decode_pair(s[i - 2], s[i - 1])) % MOD

        return dp[n]
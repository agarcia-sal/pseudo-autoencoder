class Solution:
    def numDecodings(self, s):
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        def ways_to_decode_single(char):
            if char == '*':
                return 9
            elif char == '0':
                return 0
            else:
                return 1

        def ways_to_decode_pair(char1, char2):
            if char1 == '*' and char2 == '*':
                return 15  # 11-19 and 21-26
            elif char1 == '*':
                if '0' <= char2 <= '6':
                    return 2  # * can be 1 or 2
                else:
                    return 1  # * can only be 1
            elif char2 == '*':
                if char1 == '1':
                    return 9  # 11-19
                elif char1 == '2':
                    return 6  # 21-26
                else:
                    return 0
            else:
                num = int(char1 + char2)
                return 1 if 10 <= num <= 26 else 0

        for i in range(1, n + 1):
            dp[i] = (dp[i] + dp[i - 1] * ways_to_decode_single(s[i - 1])) % MOD
            if i > 1:
                dp[i] = (dp[i] + dp[i - 2] * ways_to_decode_pair(s[i - 2], s[i - 1])) % MOD

        return dp[n]
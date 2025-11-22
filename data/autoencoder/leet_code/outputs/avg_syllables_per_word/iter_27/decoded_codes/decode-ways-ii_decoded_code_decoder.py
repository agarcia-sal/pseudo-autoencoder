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
                # "**" can represent 11-19 and 21-26 (15 possibilities)
                return 15
            elif char1 == '*':
                # '*' followed by a digit
                if '0' <= char2 <= '6':
                    # "*" can be '1' or '2' to make valid pairs with '0'-'6'
                    return 2
                elif '7' <= char2 <= '9':
                    # Only '1' valid for pairs with '7'-'9'
                    return 1
                else:
                    return 0
            elif char2 == '*':
                # digit followed by '*'
                if char1 == '1':
                    # '1*' can be 11-19 (9 possibilities)
                    return 9
                elif char1 == '2':
                    # '2*' can be 21-26 (6 possibilities)
                    return 6
                else:
                    return 0
            else:
                # Both chars are digits
                num = int(char1 + char2)
                if 10 <= num <= 26:
                    return 1
                else:
                    return 0

        for i in range(1, n + 1):
            dp[i] = (dp[i - 1] * ways_to_decode_single(s[i - 1])) % MOD

        for i in range(2, n + 1):
            dp[i] = (dp[i] + dp[i - 2] * ways_to_decode_pair(s[i - 2], s[i - 1])) % MOD

        return dp[n]
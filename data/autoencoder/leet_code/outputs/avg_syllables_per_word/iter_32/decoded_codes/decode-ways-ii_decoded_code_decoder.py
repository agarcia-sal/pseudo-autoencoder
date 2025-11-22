from typing import List

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
                # '**' can represent 11 to 19 and 21 to 26
                # 11-19: 9 options, 21-26: 6 options, total 15
                return 15
            elif char1 == '*':
                # First char is '*', second is digit
                # If second char <= '6', '*' can be '1' or '2' => 2 ways
                # else only '1' works => 1 way
                if '0' <= char2 <= '6':
                    return 2
                else:
                    return 1
            elif char2 == '*':
                # First char digit, second is '*'
                if char1 == '1':
                    return 9  # '11' to '19'
                elif char1 == '2':
                    return 6  # '21' to '26'
                else:
                    return 0
            else:
                # Both digits
                num = int(char1 + char2)
                if 10 <= num <= 26:
                    return 1
                else:
                    return 0

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] * ways_to_decode_single(s[i - 1])
            dp[i] %= MOD

            if i > 1:
                dp[i] += dp[i - 2] * ways_to_decode_pair(s[i - 2], s[i - 1])
                dp[i] %= MOD

        return dp[n]
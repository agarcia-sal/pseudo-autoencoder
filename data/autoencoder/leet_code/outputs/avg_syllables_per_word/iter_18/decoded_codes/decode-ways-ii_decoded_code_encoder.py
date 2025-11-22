class Solution:
    def numDecodings(self, s: str) -> int:
        MODULO_CONSTANT = 10**9 + 1

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        def ways_to_decode_single(c: str) -> int:
            if c == '*':
                return 9
            elif c == '0':
                return 0
            else:
                return 1

        def ways_to_decode_pair(c1: str, c2: str) -> int:
            if c1 == '*' and c2 == '*':
                return 15  # 11-19 and 21-26 total 15 possibilities
            elif c1 == '*':
                if c2 <= '6':
                    return 2  # '*' can be '1' or '2'
                else:
                    return 1  # '*' must be '1'
            elif c2 == '*':
                if c1 == '1':
                    return 9  # 11-19
                elif c1 == '2':
                    return 6  # 21-26
                else:
                    return 0
            else:
                combined = int(c1 + c2)
                if 10 <= combined <= 26:
                    return 1
                else:
                    return 0

        for i in range(1, len(s) + 1):
            dp[i] += dp[i - 1] * ways_to_decode_single(s[i - 1])
            dp[i] %= MODULO_CONSTANT

            if i > 1:
                dp[i] += dp[i - 2] * ways_to_decode_pair(s[i - 2], s[i - 1])
                dp[i] %= MODULO_CONSTANT

        return dp[-1]
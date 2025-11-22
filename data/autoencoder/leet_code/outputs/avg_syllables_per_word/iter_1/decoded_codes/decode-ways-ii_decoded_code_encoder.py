def numDecodings(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1

    def ways_single(c):
        if c == '*':
            return 9
        if c == '0':
            return 0
        return 1

    def ways_pair(c1, c2):
        if c1 == '*' and c2 == '*':
            return 15
        if c1 == '*':
            if c2 <= '6':
                return 2
            else:
                return 1
        if c2 == '*':
            if c1 == '1':
                return 9
            if c1 == '2':
                return 6
            return 0
        n = int(c1 + c2)
        return 1 if 10 <= n <= 26 else 0

    for i in range(1, n+1):
        dp[i] = (dp[i] + dp[i-1] * ways_single(s[i-1])) % MOD
        if i > 1:
            dp[i] = (dp[i] + dp[i-2] * ways_pair(s[i-2], s[i-1])) % MOD

    return dp[n]
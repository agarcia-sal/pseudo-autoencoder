def count_palindromic_subsequences(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)

    next_occ = [[-1] * n for _ in range(4)]
    prev_occ = [[-1] * n for _ in range(4)]

    for c in range(4):
        ch = chr(ord('a') + c)

        last = -1
        for i in range(n):
            if s[i] == ch:
                last = i
            prev_occ[c][i] = last

        last = -1
        for i in range(n - 1, -1, -1):
            if s[i] == ch:
                last = i
            next_occ[c][i] = last

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            val = 0
            for c in range(4):
                l = next_occ[c][i]
                r = prev_occ[c][j]
                if l == -1 or r == -1 or l > j or r < i:
                    continue
                if l == r:
                    val += 1
                else:
                    val += dp[l + 1][r - 1] + 2
            dp[i][j] = val % MOD

    return dp[0][n - 1]
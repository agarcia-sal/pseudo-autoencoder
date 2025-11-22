def min_changes(sub):
    i, j, c = 0, len(sub) - 1, 0
    while i < j:
        c += (sub[i] != sub[j])
        i += 1
        j -= 1
    return c

def palindrome_partition(s, k):
    n = len(s)
    INF = float('inf')
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, min(k, i) + 1):
            for start in range(i):
                dp[i][j] = min(dp[i][j], dp[start][j - 1] + min_changes(s[start:i]))

    return dp[n][k]
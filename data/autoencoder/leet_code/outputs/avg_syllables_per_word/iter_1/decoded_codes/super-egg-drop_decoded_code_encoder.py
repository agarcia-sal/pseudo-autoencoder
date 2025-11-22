def super_egg_drop(k, n):
    dp = [0] * (k + 1)
    moves = 0
    while dp[k] < n:
        moves += 1
        for e in range(k, 0, -1):
            dp[e] = 1 + dp[e - 1] + dp[e]
    return moves
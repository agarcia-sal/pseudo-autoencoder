def largest_plus_sign(n, mines):
    mines_set = set((x, y) for x, y in mines)
    dp = [[[0]*4 for _ in range(n)] for _ in range(n)]

    # Directions: 0 = right, 1 = down, 2 = left, 3 = up
    for i in range(n):
        for j in range(n):
            if (i, j) not in mines_set:
                dp[i][j][0] = (dp[i][j-1][0] + 1) if j > 0 else 1
                dp[i][j][1] = (dp[i-1][j][1] + 1) if i > 0 else 1

    result = 0
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if (i, j) not in mines_set:
                dp[i][j][2] = (dp[i][j+1][2] + 1) if j < n-1 else 1
                dp[i][j][3] = (dp[i+1][j][3] + 1) if i < n-1 else 1
                order = min(dp[i][j])
                result = max(result, order)

    return result
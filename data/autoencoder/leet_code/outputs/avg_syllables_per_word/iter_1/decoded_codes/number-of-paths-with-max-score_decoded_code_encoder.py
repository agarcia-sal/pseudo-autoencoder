def paths_with_max_sum(board):
    MOD = 10**9 + 7
    n = len(board)
    NEG_INF = float('-inf')

    # Initialize dp array with [max_sum, count], where max_sum is -inf and count is 0
    dp = [[[NEG_INF, 0] for _ in range(n)] for __ in range(n)]

    dp[n-1][n-1] = [0, 1]

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if board[i][j] in ['X', 'S']:
                continue
            val = 0 if board[i][j] == 'E' else int(board[i][j])
            for x, y in [(1, 0), (0, 1), (1, 1)]:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < n:
                    if dp[ni][nj][0] > dp[i][j][0]:
                        dp[i][j][0] = dp[ni][nj][0] + val
                        dp[i][j][1] = dp[ni][nj][1]
                    elif dp[ni][nj][0] == dp[i][j][0]:
                        dp[i][j][1] = (dp[i][j][1] + dp[ni][nj][1]) % MOD

    if dp[0][0][0] == NEG_INF:
        return [0, 0]
    return [dp[0][0][0], dp[0][0][1]]
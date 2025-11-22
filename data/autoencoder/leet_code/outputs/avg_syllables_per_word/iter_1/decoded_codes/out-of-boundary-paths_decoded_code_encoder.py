MOD = 10**9 + 7

def find_paths(m, n, maxMove, startRow, startColumn):
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    dp = [[[0] * (maxMove + 1) for _ in range(n)] for __ in range(m)]

    for k in range(1, maxMove + 1):
        for i in range(m):
            for j in range(n):
                total = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        total += 1
                    else:
                        total += dp[ni][nj][k-1]
                dp[i][j][k] = total % MOD

    return dp[startRow][startColumn][maxMove]
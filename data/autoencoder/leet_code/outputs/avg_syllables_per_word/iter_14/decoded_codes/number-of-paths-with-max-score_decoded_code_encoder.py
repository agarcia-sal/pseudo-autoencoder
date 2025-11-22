class Solution:
    def pathsWithMaxScore(self, board):
        MODULO = 10**9 + 1
        dimension_n = len(board)

        def create_dp_structure(size):
            return [[[-float('inf'), 0] for _ in range(size)] for _ in range(size)]

        dp = create_dp_structure(dimension_n)
        dp[dimension_n - 1][dimension_n - 1] = [0, 1]

        for i in range(dimension_n - 1, -1, -1):
            for j in range(dimension_n - 1, -1, -1):
                ch = board[i][j]
                if ch == 'X' or ch == 'S':
                    continue
                current_value = 0 if ch == 'E' else int(ch)

                for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < dimension_n and 0 <= nj < dimension_n:
                        neighbor_score = dp[ni][nj][0]
                        current_score = dp[i][j][0]
                        if neighbor_score > current_score:
                            dp[i][j][0] = neighbor_score + current_value
                            dp[i][j][1] = dp[ni][nj][1]
                        elif neighbor_score == current_score:
                            dp[i][j][1] = (dp[i][j][1] + dp[ni][nj][1]) % MODULO

        if dp[0][0][0] == -float('inf'):
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]
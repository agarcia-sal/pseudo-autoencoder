class Solution:
    def pathsWithMaxScore(self, board):
        modulus_value = 10**9 + 1
        board_size = len(board)
        # dp[r][c] = (max_score, count_of_paths)
        dp = [[(float('-inf'), 0) for _ in range(board_size)] for _ in range(board_size)]
        dp[board_size - 1][board_size - 1] = (0, 1)

        for r in range(board_size - 1, -1, -1):
            for c in range(board_size - 1, -1, -1):
                if board[r][c] in ('X', 'S'):
                    continue
                current_value = 0 if board[r][c] == 'E' else int(board[r][c])
                for dr, dc in ((1, 0), (0, 1), (1, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < board_size and 0 <= nc < board_size:
                        next_score, next_count = dp[nr][nc]
                        if next_score == float('-inf'):
                            continue
                        candidate_score = next_score + current_value
                        curr_score, curr_count = dp[r][c]
                        if candidate_score > curr_score:
                            dp[r][c] = (candidate_score, next_count)
                        elif candidate_score == curr_score:
                            dp[r][c] = (curr_score, (curr_count + next_count) % modulus_value)

        max_score, count_paths = dp[0][0]
        if max_score == float('-inf'):
            return (0, 0)
        return (max_score, count_paths)
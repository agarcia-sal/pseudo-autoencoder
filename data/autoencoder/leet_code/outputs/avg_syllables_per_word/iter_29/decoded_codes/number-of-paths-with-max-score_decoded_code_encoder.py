class Solution:
    def pathsWithMaxScore(self, board):
        MODULO = 10**9 + 7
        board_size = len(board)

        # dp_matrix[i][j] = [max_score_from_here, count_of_paths_with_max_score_from_here]
        dp_matrix = [[[-float('inf'), 0] for _ in range(board_size)] for _ in range(board_size)]
        dp_matrix[board_size - 1][board_size - 1] = [0, 1]

        for i in range(board_size - 1, -1, -1):
            for j in range(board_size - 1, -1, -1):
                if board[i][j] in ('X', 'S'):
                    continue

                current_value = 0 if board[i][j] == 'E' else int(board[i][j])

                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    new_i, new_j = i + x, j + y
                    if 0 <= new_i < board_size and 0 <= new_j < board_size:
                        next_score, next_count = dp_matrix[new_i][new_j]
                        if next_score == -float('inf'):
                            continue
                        candidate_score = next_score + current_value
                        curr_score, curr_count = dp_matrix[i][j]
                        if candidate_score > curr_score:
                            dp_matrix[i][j] = [candidate_score, next_count]
                        elif candidate_score == curr_score:
                            dp_matrix[i][j][1] = (dp_matrix[i][j][1] + next_count) % MODULO

        if dp_matrix[0][0][0] == -float('inf'):
            return [0, 0]

        return dp_matrix[0][0]
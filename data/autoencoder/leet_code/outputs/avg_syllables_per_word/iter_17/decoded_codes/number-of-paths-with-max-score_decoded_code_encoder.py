class Solution:
    def pathsWithMaxScore(self, board):
        MODULO_CONSTANT = 10**9 + 7
        size_n = len(board)

        dp = self.initialize_dp_array(size_n)
        self.set_starting_point(dp, size_n)

        # Traverse from bottom-right to top-left
        for row_index in range(size_n - 1, -1, -1):
            for column_index in range(size_n - 1, -1, -1):
                cell = board[row_index][column_index]

                # Skip start 'S' and end 'X' cells
                if cell in ('S', 'X'):
                    continue

                current_value = 0 if cell == 'E' else int(cell)

                # Offsets corresponding to moves: down (1,0), right (0,1), diagonal (1,1)
                for offset_x, offset_y in ((1, 0), (0, 1), (1, 1)):
                    new_row = row_index + offset_x
                    new_column = column_index + offset_y

                    if 0 <= new_row < size_n and 0 <= new_column < size_n:
                        dp_val_new, dp_count_new = dp[new_row][new_column]
                        dp_val_curr, dp_count_curr = dp[row_index][column_index]

                        if dp_val_new > dp_val_curr:
                            dp[row_index][column_index][0] = dp_val_new + current_value
                            dp[row_index][column_index][1] = dp_count_new
                        elif dp_val_new == dp_val_curr and dp_val_new != float('-inf'):
                            dp[row_index][column_index][1] = (dp_count_curr + dp_count_new) % MODULO_CONSTANT

        max_score, count = dp[0][0]
        if max_score == float('-inf'):
            return [0, 0]
        return [max_score, count]

    def initialize_dp_array(self, size_n):
        # Each cell is [score, paths_count], initially score = -inf, count=0
        return [[[float('-inf'), 0] for _ in range(size_n)] for _ in range(size_n)]

    def set_starting_point(self, dp, size_n):
        # Start at bottom-right with score 0 and path count 1
        dp[size_n - 1][size_n - 1][0] = 0
        dp[size_n - 1][size_n - 1][1] = 1
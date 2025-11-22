class Solution:
    def candyCrush(self, board):
        number_of_rows = len(board)
        number_of_columns = len(board[0]) if number_of_rows > 0 else 0
        stable = False

        while not stable:
            stable = True
            positions_to_crush = set()

            # Check rows for crushable candies
            for row_index in range(number_of_rows):
                for column_index in range(number_of_columns - 2):
                    val = abs(board[row_index][column_index])
                    if val != 0 and val == abs(board[row_index][column_index + 1]) == abs(board[row_index][column_index + 2]):
                        stable = False
                        positions_to_crush.add((row_index, column_index))
                        positions_to_crush.add((row_index, column_index + 1))
                        positions_to_crush.add((row_index, column_index + 2))

            # Check columns for crushable candies
            for row_index in range(number_of_rows - 2):
                for column_index in range(number_of_columns):
                    val = abs(board[row_index][column_index])
                    if val != 0 and val == abs(board[row_index + 1][column_index]) == abs(board[row_index + 2][column_index]):
                        stable = False
                        positions_to_crush.add((row_index, column_index))
                        positions_to_crush.add((row_index + 1, column_index))
                        positions_to_crush.add((row_index + 2, column_index))

            # Crush candies
            for r, c in positions_to_crush:
                board[r][c] = 0

            # Drop candies down
            for column_index in range(number_of_columns):
                write_row = number_of_rows - 1
                for row_index in range(number_of_rows - 1, -1, -1):
                    if board[row_index][column_index] != 0:
                        board[write_row][column_index] = board[row_index][column_index]
                        write_row -= 1
                for fill_row in range(write_row, -1, -1):
                    board[fill_row][column_index] = 0

        return board
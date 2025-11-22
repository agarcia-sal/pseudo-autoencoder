class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MODULO_DIVISOR = 10**9 + 7

        def generate_valid_columns(previous_column):
            available_colors = [1, 2, 3]
            valid_columns = []

            def backtrack(current_column, current_row):
                if current_row == m:
                    valid_columns.append(tuple(current_column))
                    return
                for color in available_colors:
                    if (not current_column or current_column[-1] != color) and (previous_column is None or previous_column[current_row] != color):
                        current_column.append(color)
                        backtrack(current_column, current_row + 1)
                        current_column.pop()

            backtrack([], 0)
            return valid_columns

        all_valid_columns = generate_valid_columns(None)
        number_of_valid_columns = len(all_valid_columns)

        compatible_columns = {i: [] for i in range(number_of_valid_columns)}
        for i in range(number_of_valid_columns):
            for j in range(number_of_valid_columns):
                columns_are_compatible = True
                for k in range(m):
                    if all_valid_columns[i][k] == all_valid_columns[j][k]:
                        columns_are_compatible = False
                        break
                if columns_are_compatible:
                    compatible_columns[i].append(j)

        dp = [1] * number_of_valid_columns

        for _ in range(1, n):
            next_dp = [0] * number_of_valid_columns
            for i in range(number_of_valid_columns):
                for j in compatible_columns[i]:
                    next_dp[j] = (next_dp[j] + dp[i]) % MODULO_DIVISOR
            dp = next_dp

        total_ways = sum(dp) % MODULO_DIVISOR
        return total_ways
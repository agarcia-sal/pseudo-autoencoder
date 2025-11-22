class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MODULO = 10**9 + 7

        def generate_valid_columns(previous_column):
            available_colors = [1, 2, 3]
            valid_columns = []

            def backtrack(current_column, current_row):
                if current_row == m:
                    valid_columns.append(tuple(current_column))
                    return
                for color in available_colors:
                    if not current_column or current_column[-1] != color:
                        if previous_column is not None and previous_column[current_row] == color:
                            continue
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
                col_i = all_valid_columns[i]
                col_j = all_valid_columns[j]
                for k in range(m):
                    if col_i[k] == col_j[k]:
                        columns_are_compatible = False
                        break
                if columns_are_compatible:
                    compatible_columns[i].append(j)

        dp = [1] * number_of_valid_columns

        for _ in range(1, n):
            next_dp = [0] * number_of_valid_columns
            for idx in range(number_of_valid_columns):
                ways = dp[idx]
                if ways:
                    for compatible_idx in compatible_columns[idx]:
                        next_dp[compatible_idx] = (next_dp[compatible_idx] + ways) % MODULO
            dp = next_dp

        total_ways = sum(dp) % MODULO

        return total_ways
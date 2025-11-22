class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        def generate_valid_columns(previous_column):
            colors = [1, 2, 3]
            valid_columns = []

            def backtrack(current_column, current_row):
                if current_row == m:
                    valid_columns.append(tuple(current_column))
                    return
                for color in colors:
                    if (not current_column or current_column[-1] != color) and (
                        previous_column is None or previous_column[current_row] != color
                    ):
                        current_column.append(color)
                        backtrack(current_column, current_row + 1)
                        current_column.pop()

            backtrack([], 0)
            return valid_columns

        all_valid_columns = generate_valid_columns(None)
        num_valid_columns = len(all_valid_columns)

        compatible_columns = {i: [] for i in range(num_valid_columns)}

        for i in range(num_valid_columns):
            for j in range(num_valid_columns):
                # Check if all positions differ
                different = True
                col_i = all_valid_columns[i]
                col_j = all_valid_columns[j]
                for k in range(m):
                    if col_i[k] == col_j[k]:
                        different = False
                        break
                if different:
                    compatible_columns[i].append(j)

        dp = [1] * num_valid_columns

        for _ in range(1, n):
            next_dp = [0] * num_valid_columns
            for i in range(num_valid_columns):
                ways = dp[i]
                if ways == 0:
                    continue
                for j in compatible_columns[i]:
                    next_dp[j] = (next_dp[j] + ways) % MOD
            dp = next_dp

        total_ways = sum(dp) % MOD
        return total_ways
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [1, 2, 3]

        def generate_valid_columns(prev_col):
            valid_cols = []

            def backtrack(col, row):
                if row == m:
                    valid_cols.append(tuple(col))
                    return
                for color in colors:
                    if (not col or col[-1] != color) and (not prev_col or prev_col[row] != color):
                        col.append(color)
                        backtrack(col, row + 1)
                        col.pop()

            backtrack([], 0)
            return valid_cols

        all_valid_cols = generate_valid_columns(None)
        num_valid_cols = len(all_valid_cols)

        compatible_cols = [[] for _ in range(num_valid_cols)]
        for i in range(num_valid_cols):
            col_i = all_valid_cols[i]
            for j in range(num_valid_cols):
                col_j = all_valid_cols[j]
                if all(col_i[k] != col_j[k] for k in range(m)):
                    compatible_cols[i].append(j)

        dp = [1] * num_valid_cols

        for _ in range(n - 1):
            next_dp = [0] * num_valid_cols
            for i in range(num_valid_cols):
                for j in compatible_cols[i]:
                    next_dp[j] = (next_dp[j] + dp[i]) % MOD
            dp = next_dp

        return sum(dp) % MOD
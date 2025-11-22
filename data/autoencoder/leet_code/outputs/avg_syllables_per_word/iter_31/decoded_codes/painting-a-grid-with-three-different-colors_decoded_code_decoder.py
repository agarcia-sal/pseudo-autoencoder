from typing import List, Optional

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 1

        def generate_valid_columns(prev_col: Optional[List[int]]) -> List[tuple]:
            colors = [1, 2, 3]
            valid_cols = []

            def backtrack(col: List[int], row: int):
                if row == m:
                    valid_cols.append(tuple(col))
                    return
                for color in colors:
                    if not col or col[-1] != color:
                        if prev_col is not None and prev_col[row] == color:
                            continue
                        col.append(color)
                        backtrack(col, row + 1)
                        col.pop()

            backtrack([], 0)
            return valid_cols

        all_valid_cols = generate_valid_columns(None)
        num_valid_cols = len(all_valid_cols)

        compatible_cols = {i: [] for i in range(num_valid_cols)}

        for i in range(num_valid_cols):
            col_i = all_valid_cols[i]
            for j in range(num_valid_cols):
                col_j = all_valid_cols[j]
                valid_flag = True
                for k in range(m):
                    if col_i[k] == col_j[k]:
                        valid_flag = False
                        break
                if valid_flag:
                    compatible_cols[i].append(j)

        dp = [1] * num_valid_cols

        for _ in range(1, n):
            next_dp = [0] * num_valid_cols
            for i in range(num_valid_cols):
                dp_i = dp[i]
                if dp_i == 0:
                    continue
                for j in compatible_cols[i]:
                    next_dp[j] = (next_dp[j] + dp_i) % MOD
            dp = next_dp

        return sum(dp) % MOD
from typing import List, Optional

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        def generate_valid_columns(prev_col: Optional[List[int]]) -> List[tuple]:
            colors = [1, 2, 3]
            valid_cols = []

            def backtrack(col: List[int], row: int) -> None:
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
            for j in range(num_valid_cols):
                if all(all_valid_cols[i][k] != all_valid_cols[j][k] for k in range(m)):
                    compatible_cols[i].append(j)

        dp = [1] * num_valid_cols

        for _ in range(n - 1):
            next_dp = [0] * num_valid_cols
            for i in range(num_valid_cols):
                val = dp[i]
                if val == 0:
                    continue
                for j in compatible_cols[i]:
                    next_dp[j] = (next_dp[j] + val) % MOD
            dp = next_dp

        return sum(dp) % MOD
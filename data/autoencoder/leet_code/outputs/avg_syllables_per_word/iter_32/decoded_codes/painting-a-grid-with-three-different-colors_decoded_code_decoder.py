from typing import List, Tuple, Optional

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        def generate_valid_columns(prev_col: Optional[Tuple[int, ...]]) -> List[Tuple[int, ...]]:
            colors = [1, 2, 3]
            valid_cols = []

            def backtrack(col: List[int], row: int) -> None:
                if row == m:
                    valid_cols.append(tuple(col))
                    return
                for color in colors:
                    if (not col or col[-1] != color) and (prev_col is None or prev_col[row] != color):
                        col.append(color)
                        backtrack(col, row + 1)
                        col.pop()

            backtrack([], 0)
            return valid_cols

        all_valid_cols = generate_valid_columns(None)
        num_valid_cols = len(all_valid_cols)

        # Precompute compatible columns: for each column i, find all columns j that can follow it
        compatible_cols = {i: [] for i in range(num_valid_cols)}
        for i in range(num_valid_cols):
            col_i = all_valid_cols[i]
            for j in range(num_valid_cols):
                col_j = all_valid_cols[j]
                # Check compatibility: no row has the same color in col_i and col_j
                if all(col_i[k] != col_j[k] for k in range(m)):
                    compatible_cols[i].append(j)

        dp = [1] * num_valid_cols  # ways to paint first column

        for _ in range(1, n):
            next_dp = [0] * num_valid_cols
            for i in range(num_valid_cols):
                ways = dp[i]
                if ways == 0:
                    continue
                for j in compatible_cols[i]:
                    next_dp[j] = (next_dp[j] + ways) % MOD
            dp = next_dp

        total_ways = sum(dp) % MOD
        return total_ways
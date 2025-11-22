from typing import List, Tuple, Optional

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [1, 2, 3]

        def generate_valid_columns(prev_col: Optional[Tuple[int, ...]]) -> List[Tuple[int, ...]]:
            valid_cols: List[Tuple[int, ...]] = []

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

        compatible_cols = {i: [] for i in range(num_valid_cols)}
        # Precompute compatibility: columns are compatible if no cell in same row shares the same color
        for i in range(num_valid_cols):
            col_i = all_valid_cols[i]
            for j in range(num_valid_cols):
                col_j = all_valid_cols[j]
                # All rows k satisfy col_i[k] != col_j[k]
                if all(col_i[k] != col_j[k] for k in range(m)):
                    compatible_cols[i].append(j)

        dp = [1] * num_valid_cols
        for _ in range(n - 1):
            next_dp = [0] * num_valid_cols
            for i in range(num_valid_cols):
                val = dp[i]
                if val:
                    for j in compatible_cols[i]:
                        next_dp[j] = (next_dp[j] + val) % MOD
            dp = next_dp

        return sum(dp) % MOD
from typing import List, Tuple, Optional

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [1, 2, 3]

        def generate_valid_columns(prev_col: Optional[Tuple[int, ...]]) -> List[Tuple[int, ...]]:
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
            col_i = all_valid_cols[i]
            for j in range(num_valid_cols):
                col_j = all_valid_cols[j]
                # Check if columns i and j have different colors in all rows
                all_elements_different = True
                for k in range(m):
                    if col_i[k] == col_j[k]:
                        all_elements_different = False
                        break
                if all_elements_different:
                    compatible_cols[i].append(j)

        dp = [1] * num_valid_cols

        for _ in range(n - 1):
            next_dp = [0] * num_valid_cols
            for i in range(num_valid_cols):
                ways_i = dp[i]
                for j in compatible_cols[i]:
                    next_dp[j] = (next_dp[j] + ways_i) % MOD
            dp = next_dp

        total_ways = sum(dp) % MOD
        return total_ways
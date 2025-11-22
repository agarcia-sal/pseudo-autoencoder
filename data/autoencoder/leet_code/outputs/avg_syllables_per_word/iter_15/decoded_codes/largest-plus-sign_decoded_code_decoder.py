from typing import List, Set, Tuple

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set: Set[Tuple[int, int]] = set(map(tuple, mines))
        dp: List[List[List[int]]] = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

        # Traverse from top-left to bottom-right to count consecutive 1s from left and top
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1  # left to right count
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1  # top to bottom count

        result = 0

        # Traverse from bottom-right to top-left to count consecutive 1s from right and bottom
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if (i, j) not in mines_set:
                    dp[i][j][2] = dp[i][j+1][2] + 1 if j < n - 1 else 1  # right to left count
                    dp[i][j][3] = dp[i+1][j][3] + 1 if i < n - 1 else 1  # bottom to top count

                    # The order of plus sign is minimum arm length in all four directions
                    plus_sign_order = min(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result
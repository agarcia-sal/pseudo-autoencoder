from typing import List, Set, Tuple

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = self.convert_mines_to_set(mines)
        dp = self.initialize_dp_grid(n)
        directions = self.define_directions()  # directions not used in logic but preserved as per spec

        # Left to right & Top to bottom
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    if j > 0:
                        dp[i][j][0] = dp[i][j - 1][0] + 1
                    else:
                        dp[i][j][0] = 1
                    if i > 0:
                        dp[i][j][1] = dp[i - 1][j][1] + 1
                    else:
                        dp[i][j][1] = 1

        result = 0

        # Right to left & Bottom to top
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    if j < n - 1:
                        dp[i][j][2] = dp[i][j + 1][2] + 1
                    else:
                        dp[i][j][2] = 1
                    if i < n - 1:
                        dp[i][j][3] = dp[i + 1][j][3] + 1
                    else:
                        dp[i][j][3] = 1
                    plus_sign_order = self.minimum_value(dp[i][j])
                    if plus_sign_order > result:
                        result = plus_sign_order

        return result

    def convert_mines_to_set(self, mines: List[List[int]]) -> Set[Tuple[int, int]]:
        mines_set = set()
        for mine in mines:
            mines_set.add((mine[0], mine[1]))
        return mines_set

    def initialize_dp_grid(self, n: int) -> List[List[List[int]]]:
        grid = []
        for _ in range(n):
            row = [[0, 0, 0, 0] for _ in range(n)]
            grid.append(row)
        return grid

    def define_directions(self) -> List[Tuple[int, int]]:
        return [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def minimum_value(self, list_of_values: List[int]) -> int:
        min_value = list_of_values[0]
        for value in list_of_values:
            if value < min_value:
                min_value = value
        return min_value
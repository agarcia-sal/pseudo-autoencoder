from typing import List, Set, Tuple

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, direction: str) -> List[str]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(direction)
                dfs(i + 1, j, 'D')  # Down
                dfs(i - 1, j, 'U')  # Up
                dfs(i, j + 1, 'R')  # Right
                dfs(i, j - 1, 'L')  # Left
                path.append('B')    # Backtrack
            return path

        unique_islands: Set[Tuple[str, ...]] = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    shape = dfs(i, j, 'O')  # Origin
                    unique_islands.add(tuple(shape))

        return len(unique_islands)
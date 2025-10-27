from typing import List, Set, Tuple

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, direction: str) -> None:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0  # mark visited
                path.append(direction)
                dfs(i + 1, j, 'd')  # down
                dfs(i - 1, j, 'u')  # up
                dfs(i, j + 1, 'r')  # right
                dfs(i, j - 1, 'l')  # left
                path.append('b')  # backtracking marker

        unique_islands: Set[Tuple[str, ...]] = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path: List[str] = []
                    dfs(i, j, 'o')  # origin
                    unique_islands.add(tuple(path))

        return len(unique_islands)
from typing import List, Set, Tuple

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, direction: str) -> List[str]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(direction)
                dfs(i + 1, j, 'd')  # down
                dfs(i - 1, j, 'u')  # up
                dfs(i, j + 1, 'r')  # right
                dfs(i, j - 1, 'l')  # left
                path.append('b')  # backtrack
            return path

        unique_islands: Set[Tuple[str, ...]] = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    unique_islands.add(tuple(dfs(i, j, 'o')))  # origin

        return len(unique_islands)
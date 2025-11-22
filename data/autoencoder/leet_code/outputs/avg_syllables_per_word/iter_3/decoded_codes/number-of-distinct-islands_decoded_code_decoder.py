class Solution:
    def numDistinctIslands(self, grid):
        def dfs(i, j, direction):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(direction)
                dfs(i + 1, j, 'd')
                dfs(i - 1, j, 'u')
                dfs(i, j + 1, 'r')
                dfs(i, j - 1, 'l')
                path.append('b')
            return path

        unique_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    unique_islands.add(tuple(dfs(i, j, 'o')))
        return len(unique_islands)
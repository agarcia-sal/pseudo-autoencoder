class Solution:
    def numDistinctIslands(self, grid):
        def dfs(i, j, direction):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(direction)
                dfs(i + 1, j, 'd')  # down
                dfs(i - 1, j, 'u')  # up
                dfs(i, j + 1, 'r')  # right
                dfs(i, j - 1, 'l')  # left
                path.append('b')    # backtracking step
            return path

        unique_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    unique_islands.add(tuple(dfs(i, j, 'o')))  # 'o' for origin
        return len(unique_islands)
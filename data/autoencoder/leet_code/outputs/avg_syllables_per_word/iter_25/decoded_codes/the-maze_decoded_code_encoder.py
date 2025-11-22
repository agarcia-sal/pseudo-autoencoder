from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(maze), len(maze[0])
        visited = set()

        def dfs(x: int, y: int) -> bool:
            if (x, y) in visited:
                return False
            if [x, y] == destination:
                return True
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x, y
                # roll the ball until it hits a wall or boundary
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                if dfs(nx, ny):
                    return True

            return False

        return dfs(start[0], start[1])
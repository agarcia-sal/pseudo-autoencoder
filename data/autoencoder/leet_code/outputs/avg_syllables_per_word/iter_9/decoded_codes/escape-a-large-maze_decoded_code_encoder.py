from collections import deque

class Solution:
    def isEscapePossible(self, blocked, source, target):
        if not blocked:
            return True

        blocked_set = {tuple(b) for b in blocked}
        n = len(blocked)
        max_steps = n * (n - 1) // 2

        def bfs(start, end):
            queue = deque([tuple(start)])
            visited = {tuple(start)}
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            while queue:
                x, y = queue.popleft()
                if len(visited) > max_steps or (x, y) == tuple(end):
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in blocked_set and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return False

        return bfs(source, target) and bfs(target, source)
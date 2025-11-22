from collections import deque
from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True

        blocked_set = {tuple(b) for b in blocked}
        n = len(blocked)
        max_steps = n * (n - 1) // 2

        def bfs(start: List[int], end: List[int]) -> bool:
            queue = deque([tuple(start)])
            visited = set(queue)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                x, y = queue.popleft()
                if len(visited) > max_steps or (x == end[0] and y == end[1]):
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6:
                        if (nx, ny) not in blocked_set and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            return False

        return bfs(source, target) and bfs(target, source)
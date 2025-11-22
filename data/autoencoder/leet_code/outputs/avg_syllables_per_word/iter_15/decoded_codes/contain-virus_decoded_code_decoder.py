from collections import deque
from typing import List, Set, Tuple

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0]) if isInfected else 0

        def neighbors(r: int, c: int) -> List[Tuple[int, int]]:
            return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        def bfs(r: int, c: int) -> Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]]]:
            infected = set()
            threatened = set()
            queue = deque([(r, c)])
            visited_local = {(r, c)}
            while queue:
                x, y = queue.popleft()
                infected.add((x, y))
                for nx, ny in neighbors(x, y):
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited_local:
                        visited_local.add((nx, ny))
                        if isInfected[nx][ny] == 1:
                            queue.append((nx, ny))
                        elif isInfected[nx][ny] == 0:
                            threatened.add((nx, ny))
            return infected, threatened

        def build_walls(infected: Set[Tuple[int, int]]) -> int:
            walls = 0
            for x, y in infected:
                for nx, ny in neighbors(x, y):
                    if 0 <= nx < m and 0 <= ny < n and isInfected[nx][ny] == 0:
                        walls += 1
            return walls

        def spread_virus(threatened: Set[Tuple[int, int]]) -> None:
            for x, y in threatened:
                isInfected[x][y] = 1

        total_walls = 0

        while True:
            regions = []
            visited = set()
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        infected, threatened = bfs(r, c)
                        regions.append((infected, threatened))
                        visited |= infected

            if not regions:
                break

            # Sort regions by the size of their threatened set descending
            regions.sort(key=lambda x: -len(x[1]))

            # Build walls around the region with the most threatened neighbors
            quarantined_infected, quarantined_threatened = regions[0]
            total_walls += build_walls(quarantined_infected)

            # Mark quarantined infected cells as -1
            for x, y in quarantined_infected:
                isInfected[x][y] = -1

            # Spread virus for all other regions
            for i in range(1, len(regions)):
                spread_virus(regions[i][1])

        return total_walls
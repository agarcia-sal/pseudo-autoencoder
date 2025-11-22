from collections import defaultdict, deque
from math import inf

class Solution:
    def isPrintable(self, targetGrid):
        color_bounds = defaultdict(lambda: [inf, inf, -inf, -inf])  # [minr, minc, maxr, maxc]
        rows = len(targetGrid)
        cols = len(targetGrid[0]) if rows > 0 else 0

        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                bounds = color_bounds[color]
                if r < bounds[0]:
                    bounds[0] = r
                if c < bounds[1]:
                    bounds[1] = c
                if r > bounds[2]:
                    bounds[2] = r
                if c > bounds[3]:
                    bounds[3] = c

        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for color, (minr, minc, maxr, maxc) in color_bounds.items():
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    curr_color = targetGrid[r][c]
                    if curr_color != color:
                        graph[curr_color].append(color)
                        in_degree[color] += 1

            if color not in in_degree:
                in_degree[color] = in_degree.get(color, 0)

        queue = deque(color for color in color_bounds if in_degree[color] == 0)
        visited_colors = 0

        while queue:
            color = queue.popleft()
            visited_colors += 1
            for next_color in graph[color]:
                in_degree[next_color] -= 1
                if in_degree[next_color] == 0:
                    queue.append(next_color)

        return visited_colors == len(color_bounds)
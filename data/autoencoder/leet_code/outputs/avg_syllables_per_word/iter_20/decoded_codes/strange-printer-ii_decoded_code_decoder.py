from collections import defaultdict, deque
from math import inf
from typing import List

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        color_bounds = defaultdict(lambda: [inf, inf, -inf, -inf])
        for r in range(len(targetGrid)):
            for c in range(len(targetGrid[0])):
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
        # Initialize in_degree keys for all colors to zero to avoid key errors later
        for color in color_bounds.keys():
            in_degree[color] = 0

        for color, (min_r, min_c, max_r, max_c) in color_bounds.items():
            for r in range(min_r, max_r + 1):
                row = targetGrid[r]
                for c in range(min_c, max_c + 1):
                    cell_color = row[c]
                    if cell_color != color:
                        graph[cell_color].append(color)
                        in_degree[color] += 1

        queue = deque([color for color in color_bounds if in_degree[color] == 0])
        visited_colors = 0

        while queue:
            color = queue.popleft()
            visited_colors += 1
            for next_color in graph[color]:
                in_degree[next_color] -= 1
                if in_degree[next_color] == 0:
                    queue.append(next_color)

        return visited_colors == len(color_bounds)
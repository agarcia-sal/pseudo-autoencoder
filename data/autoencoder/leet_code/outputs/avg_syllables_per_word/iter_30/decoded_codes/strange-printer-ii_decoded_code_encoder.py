from collections import defaultdict, deque
from math import inf
from typing import List

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        color_bounds = defaultdict(lambda: [inf, inf, -inf, -inf])
        rows, cols = len(targetGrid), len(targetGrid[0])

        # Determine the bounding rectangle for each color
        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                bounds = color_bounds[color]
                bounds[0] = min(bounds[0], r)  # min row
                bounds[1] = min(bounds[1], c)  # min col
                bounds[2] = max(bounds[2], r)  # max row
                bounds[3] = max(bounds[3], c)  # max col

        graph = defaultdict(list)
        in_degree = defaultdict(int)

        # Build graph edges based on color overlapping within bounding rectangles
        for color, (minr, minc, maxr, maxc) in color_bounds.items():
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    curr_color = targetGrid[r][c]
                    if curr_color != color:
                        graph[curr_color].append(color)
                        in_degree[color] += 1

        queue = deque(color for color in color_bounds if in_degree[color] == 0)
        visited_colors = 0

        # Topological sort to check if all colors can be printed in order
        while queue:
            color = queue.popleft()
            visited_colors += 1
            for next_color in graph[color]:
                in_degree[next_color] -= 1
                if in_degree[next_color] == 0:
                    queue.append(next_color)

        return visited_colors == len(color_bounds)
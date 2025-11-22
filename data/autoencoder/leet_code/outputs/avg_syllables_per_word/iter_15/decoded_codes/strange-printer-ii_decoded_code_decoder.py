from collections import defaultdict, deque
import math

class Solution:
    def isPrintable(self, targetGrid):
        color_bounds = defaultdict(lambda: [math.inf, math.inf, -math.inf, -math.inf])
        rows = len(targetGrid)
        cols = len(targetGrid[0]) if rows > 0 else 0

        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                bounds = color_bounds[color]
                # update min row and min col
                if r < bounds[0]:
                    bounds[0] = r
                if c < bounds[1]:
                    bounds[1] = c
                # update max row and max col
                if r > bounds[2]:
                    bounds[2] = r
                if c > bounds[3]:
                    bounds[3] = c

        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for color, (minr, minc, maxr, maxc) in color_bounds.items():
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    cur_color = targetGrid[r][c]
                    if cur_color != color:
                        graph[cur_color].append(color)
                        in_degree[color] += 1

        queue = deque([c for c in color_bounds if in_degree[c] == 0])
        visited_colors = 0

        while queue:
            color = queue.popleft()
            visited_colors += 1
            for next_color in graph[color]:
                in_degree[next_color] -= 1
                if in_degree[next_color] == 0:
                    queue.append(next_color)

        return visited_colors == len(color_bounds)
from collections import defaultdict, deque
import math

class Solution:
    def isPrintable(self, targetGrid):
        color_bounds = defaultdict(lambda: [math.inf, math.inf, -math.inf, -math.inf])

        for r in range(len(targetGrid)):
            for c in range(len(targetGrid[0])):
                color = targetGrid[r][c]
                color_bounds[color][0] = min(color_bounds[color][0], r)
                color_bounds[color][1] = min(color_bounds[color][1], c)
                color_bounds[color][2] = max(color_bounds[color][2], r)
                color_bounds[color][3] = max(color_bounds[color][3], c)

        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for color, (minr, minc, maxr, maxc) in color_bounds.items():
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    if targetGrid[r][c] != color:
                        other_color = targetGrid[r][c]
                        graph[other_color].append(color)
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
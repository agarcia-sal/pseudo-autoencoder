from collections import defaultdict, deque
from math import inf

class Solution:
    def isPrintable(self, targetGrid):
        color_bounds = self.initialize_color_bounds()
        rows, cols = len(targetGrid), len(targetGrid[0])

        # Determine bounding box for each color
        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                bounds = color_bounds[color]
                bounds[0] = min(bounds[0], r)  # min row
                bounds[1] = min(bounds[1], c)  # min col
                bounds[2] = max(bounds[2], r)  # max row
                bounds[3] = max(bounds[3], c)  # max col

        graph = self.initialize_graph()
        in_degree = self.initialize_in_degree()

        # Build graph and in-degree counts
        for color, (minr, minc, maxr, maxc) in color_bounds.items():
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    current_color = targetGrid[r][c]
                    if current_color != color:
                        graph[current_color].append(color)
                        in_degree[color] += 1

        # Initialize queue with colors having zero in-degree
        queue = self.initialize_queue([color for color in color_bounds if in_degree[color] == 0])
        visited_colors = 0

        while queue:
            color = queue.popleft()
            visited_colors += 1
            for next_color in graph[color]:
                in_degree[next_color] -= 1
                if in_degree[next_color] == 0:
                    queue.append(next_color)

        return visited_colors == len(color_bounds)

    def initialize_color_bounds(self):
        # Returns a dict mapping color to [min_row, min_col, max_row, max_col]
        # Initialize min_row and min_col with inf, max_row and max_col with -inf
        return defaultdict(lambda: [inf, inf, -inf, -inf])

    def initialize_graph(self):
        # Graph represented as adjacency list: color -> list of dependent colors
        return defaultdict(list)

    def initialize_in_degree(self):
        # In-degree of each node (color)
        return defaultdict(int)

    def initialize_queue(self, parameters):
        return deque(parameters)
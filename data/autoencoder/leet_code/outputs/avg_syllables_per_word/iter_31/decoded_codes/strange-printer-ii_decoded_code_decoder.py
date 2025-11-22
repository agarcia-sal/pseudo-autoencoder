from collections import defaultdict, deque

class Solution:
    def isPrintable(self, targetGrid):
        color_bounds = defaultdict(lambda: [float('inf'), float('inf'), float('-inf'), float('-inf')])
        rows = len(targetGrid)
        cols = len(targetGrid[0]) if rows else 0

        # Determine bounding boxes for each color
        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                bounds = color_bounds[color]
                # Update bounding box: min row, min col, max row, max col
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

        # Build graph edges based on color overlap in bounding boxes
        for color, (minr, minc, maxr, maxc) in color_bounds.items():
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    other_color = targetGrid[r][c]
                    if other_color != color:
                        # Color must be printed after other_color
                        graph[other_color].append(color)
                        in_degree[color] += 1

        # Initialize queue with colors having zero in-degree
        queue = deque([color for color in color_bounds if in_degree[color] == 0])
        visited_colors = 0

        # Perform topological sort
        while queue:
            color = queue.popleft()
            visited_colors += 1
            for next_color in graph[color]:
                in_degree[next_color] -= 1
                if in_degree[next_color] == 0:
                    queue.append(next_color)

        return visited_colors == len(color_bounds)
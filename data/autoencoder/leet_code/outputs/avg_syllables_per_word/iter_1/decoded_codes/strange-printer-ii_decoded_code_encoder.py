from collections import defaultdict, deque

def check_colors(grid):
    rows, cols = len(grid), len(grid[0])
    colors = set(c for row in grid for c in row)
    bounds = {color: [float('inf'), float('inf'), float('-inf'), float('-inf')] for color in colors}

    for r in range(rows):
        for c in range(cols):
            color = grid[r][c]
            minr, minc, maxr, maxc = bounds[color]
            bounds[color] = [
                min(minr, r),
                min(minc, c),
                max(maxr, r),
                max(maxc, c)
            ]

    graph = defaultdict(set)
    indeg = {color: 0 for color in colors}

    for color, (minr, minc, maxr, maxc) in bounds.items():
        for r in range(minr, maxr + 1):
            for c in range(minc, maxc + 1):
                if grid[r][c] != color:
                    if color not in graph[grid[r][c]]:
                        graph[grid[r][c]].add(color)
                        indeg[color] += 1

    queue = deque([color for color in colors if indeg[color] == 0])
    visited = 0

    while queue:
        color = queue.popleft()
        visited += 1
        for nxt in graph[color]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)

    return visited == len(colors)
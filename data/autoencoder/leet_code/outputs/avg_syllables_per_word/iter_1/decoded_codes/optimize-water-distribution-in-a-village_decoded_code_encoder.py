def minCostToSupplyWater(n, wells, pipes):
    # Add virtual node 0 with edges to each well
    for i in range(1, n + 1):
        pipes.append((0, i, wells[i - 1]))

    # Sort pipes by cost
    pipes.sort(key=lambda x: x[2])

    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
            return True
        return False

    min_cost = 0
    for h1, h2, c in pipes:
        if union(h1, h2):
            min_cost += c

    return min_cost
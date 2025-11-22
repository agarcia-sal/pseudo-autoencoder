from collections import deque
from itertools import combinations

def count_subtree_diameters(n, edges):
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(subtree):
        start = next(iter(subtree))
        Q = deque([start])
        visited = {start}
        far_node = start

        while Q:
            node = Q.popleft()
            for nbr in graph[node]:
                if nbr in subtree and nbr not in visited:
                    visited.add(nbr)
                    Q.append(nbr)
                    far_node = nbr

        Q = deque([far_node])
        visited = {far_node}
        dist = 0

        while Q:
            size = len(Q)
            for _ in range(size):
                node = Q.popleft()
                for nbr in graph[node]:
                    if nbr in subtree and nbr not in visited:
                        visited.add(nbr)
                        Q.append(nbr)
            if Q:
                dist += 1
        return dist

    res = [0] * (n-1)

    nodes = list(range(1, n+1))
    for size in range(2, n+1):
        for subset in combinations(nodes, size):
            subtree = set(subset)
            visited = set()
            stack = [subset[0]]

            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for nbr in graph[node]:
                        if nbr in subtree and nbr not in visited:
                            stack.append(nbr)

            if visited == subtree:
                d = bfs(subtree)
                if d > 0:
                    res[d-1] += 1

    return res
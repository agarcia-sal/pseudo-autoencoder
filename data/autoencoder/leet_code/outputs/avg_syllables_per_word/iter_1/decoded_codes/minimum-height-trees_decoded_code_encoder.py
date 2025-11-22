from collections import defaultdict, deque

def find_leaves(n, edges):
    if n == 1:
        return [0]

    graph = defaultdict(list)
    degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    leaves = deque(i for i in range(n) if degree[i] == 1)

    remain = n
    while remain > 2:
        count = len(leaves)
        remain -= count
        for _ in range(count):
            leaf = leaves.popleft()
            for nbr in graph[leaf]:
                degree[nbr] -= 1
                if degree[nbr] == 1:
                    leaves.append(nbr)

    return list(leaves)
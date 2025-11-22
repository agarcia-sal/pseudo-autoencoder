from collections import defaultdict, deque
from math import inf

def solve(edges, query):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def find_path(s, e):
        q = deque([(s, [s])])
        vis = {s}
        while q:
            n, p = q.popleft()
            if n == e:
                return p
            for nbr in graph[n]:
                if nbr not in vis:
                    vis.add(nbr)
                    q.append((nbr, p + [nbr]))

    def closest_node_on_path(path, node):
        min_d, closest = inf, None
        for p in path:
            d = len(find_path(p, node)) - 1
            if d < min_d:
                min_d, closest = d, p
        return closest

    answer = []
    for s, e, n in query:
        p = find_path(s, e)
        answer.append(closest_node_on_path(p, n))

    return answer
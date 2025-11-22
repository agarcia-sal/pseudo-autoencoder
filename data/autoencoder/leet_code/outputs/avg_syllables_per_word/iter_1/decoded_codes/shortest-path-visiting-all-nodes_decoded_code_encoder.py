from collections import deque

def shortest_path_visiting_all_nodes(graph):
    n = len(graph)
    q = deque((i, 1 << i) for i in range(n))
    visited = set((i, 1 << i) for i in range(n))
    all_visited = (1 << n) - 1
    steps = 0

    while q:
        for _ in range(len(q)):
            node, mask = q.popleft()
            if mask == all_visited:
                return steps
            for nxt in graph[node]:
                nxt_mask = mask | (1 << nxt)
                state = (nxt, nxt_mask)
                if state not in visited:
                    visited.add(state)
                    q.append(state)
        steps += 1

    return -1
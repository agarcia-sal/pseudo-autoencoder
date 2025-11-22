from collections import deque

def findOrder(numCourses, prerequisites):
    adj = {c: [] for c in range(numCourses)}
    indeg = [0] * numCourses

    for d, s in prerequisites:
        adj[s].append(d)
        indeg[d] += 1

    q = deque([c for c in range(numCourses) if indeg[c] == 0])
    order = []

    while q:
        cur = q.popleft()
        order.append(cur)
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)

    return order if len(order) == numCourses else []
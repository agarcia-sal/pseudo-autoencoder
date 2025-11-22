from collections import deque
import math

def minimum_time(n, edges, time, change):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    minTimes = [[math.inf, math.inf] for _ in range(n + 1)]
    minTimes[1][0] = 0

    queue = deque()
    queue.append((1, 0, 0))

    while queue:
        cur, t, c = queue.popleft()
        if cur == n and c == 1:
            return t

        if (t // change) % 2 == 0:
            wait = 0
        else:
            wait = ((t // change) + 1) * change - t

        nextT = t + wait + time

        for nei in graph[cur]:
            if nextT < minTimes[nei][0]:
                minTimes[nei][1] = minTimes[nei][0]
                minTimes[nei][0] = nextT
                queue.append((nei, nextT, 0))
            elif minTimes[nei][0] < nextT < minTimes[nei][1]:
                minTimes[nei][1] = nextT
                queue.append((nei, nextT, 1))

    return -1
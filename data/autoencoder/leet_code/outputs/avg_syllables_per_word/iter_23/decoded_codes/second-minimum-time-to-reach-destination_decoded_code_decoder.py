from collections import deque
from math import inf

class Solution:
    def secondMinimum(self, n, edges, time, change):
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 0, 0)])  # (current_node, current_time, count)
        minTimes = [[inf, inf] for _ in range(n + 1)]
        minTimes[1][0] = 0

        while queue:
            current, currentTime, count = queue.popleft()

            if current == n and count == 1:
                return currentTime

            divisionResult = currentTime // change
            remainderCheck = divisionResult % 2

            if remainderCheck == 0:
                nextTime = currentTime + time
            else:
                nextTime = (divisionResult + 1) * change + time

            for neighbor in graph[current]:
                if nextTime < minTimes[neighbor][0]:
                    minTimes[neighbor][1] = minTimes[neighbor][0]
                    minTimes[neighbor][0] = nextTime
                    queue.append((neighbor, nextTime, 0))
                elif minTimes[neighbor][0] < nextTime < minTimes[neighbor][1]:
                    minTimes[neighbor][1] = nextTime
                    queue.append((neighbor, nextTime, 1))

        return -1
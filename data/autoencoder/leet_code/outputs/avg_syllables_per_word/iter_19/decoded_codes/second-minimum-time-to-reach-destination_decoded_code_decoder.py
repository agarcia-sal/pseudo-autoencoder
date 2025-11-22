from collections import deque
from math import inf

class Solution:
    def secondMinimum(self, n, edges, time, change):
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 0, 0)])  # (current node, current time, count)
        minTimes = [[inf, inf] for _ in range(n + 1)]
        minTimes[1][0] = 0

        while queue:
            current, currentTime, count = queue.popleft()

            if current == n and count == 1:
                return currentTime

            quotient = currentTime // change
            remainder = quotient % 2
            if remainder == 0:
                nextTime = currentTime + time
            else:
                # Waiting for green signal: next green start = (quotient + 1) * change
                nextTime = (quotient + 1) * change + time

            for neighbor in graph[current]:
                first, second = minTimes[neighbor]
                if nextTime < first:
                    minTimes[neighbor][1] = first
                    minTimes[neighbor][0] = nextTime
                    queue.append((neighbor, nextTime, 0))
                elif first < nextTime < second:
                    minTimes[neighbor][1] = nextTime
                    queue.append((neighbor, nextTime, 1))

        return -1
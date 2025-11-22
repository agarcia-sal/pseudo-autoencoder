from collections import deque
from math import inf
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 0, 0)])  # node=1 (start), currentTime=0, count=0 (0 means first arrival, 1 means second)
        minTimes = [[inf, inf] for _ in range(n + 1)]
        minTimes[1][0] = 0

        while queue:
            current, currentTime, count = queue.popleft()

            if current == n and count == 1:
                return currentTime

            div, remainder = divmod(currentTime // change, 2)
            if remainder == 0:
                nextTime = currentTime + time
            else:
                nextTime = (div + 1) * change + time

            for neighbor in graph[current]:
                if minTimes[neighbor][0] > nextTime:
                    minTimes[neighbor][1] = minTimes[neighbor][0]
                    minTimes[neighbor][0] = nextTime
                    queue.append((neighbor, nextTime, 0))
                elif minTimes[neighbor][0] < nextTime < minTimes[neighbor][1]:
                    minTimes[neighbor][1] = nextTime
                    queue.append((neighbor, nextTime, 1))

        return -1
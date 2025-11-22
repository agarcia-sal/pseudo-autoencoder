from collections import deque
from math import inf

class Solution:
    def secondMinimum(self, n: int, time: int, edges: list[list[int]], change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # minTimes[node] = [shortest_time, second_shortest_time]
        minTimes = [[inf, inf] for _ in range(n + 1)]
        minTimes[1][0] = 0

        # queue elements: (current_vertex, current_time, count_of_paths: 0=shortest,1=second_shortest)
        queue = deque([(1, 0, 0)])

        while queue:
            current, currentTime, count = queue.popleft()

            if current == n and count == 1:
                return currentTime

            # Determine nextTime considering the change intervals (signal red/green)
            cycles = currentTime // change
            if cycles % 2 == 0:
                # green signal: can proceed immediately
                nextTime = currentTime + time
            else:
                # red signal: must wait until green signal comes
                nextTime = (cycles + 1) * change + time

            for neighbor in graph[current]:
                shortest, second_shortest = minTimes[neighbor]

                if nextTime < shortest:
                    # update shortest and push previous shortest to second shortest
                    minTimes[neighbor][1] = shortest
                    minTimes[neighbor][0] = nextTime
                    queue.append((neighbor, nextTime, 0))
                elif shortest < nextTime < second_shortest:
                    # update second shortest
                    minTimes[neighbor][1] = nextTime
                    queue.append((neighbor, nextTime, 1))

        return -1
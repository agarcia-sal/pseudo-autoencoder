from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = list(zip(capital, profits))
        projects.sort(key=lambda x: x[0])

        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            w += -heappop(max_heap)

        return w
from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapify(max_heap)
        time = 0
        queue = []

        while max_heap or queue:
            # Release tasks whose cooldown has finished
            while queue and queue[0][0] == time:
                _, count = queue.pop(0)
                if count < 0:
                    heappush(max_heap, count)
            if max_heap:
                count = heappop(max_heap) + 1  # Use one count
                if count < 0:
                    queue.append((time + n + 1, count))
            time += 1

        return time
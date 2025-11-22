from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = []

        while max_heap or queue:
            while queue and queue[0][0] == time:
                _, count = queue.pop(0)
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count < 0:
                    queue.append((time + n + 1, count))
            time += 1

        return time
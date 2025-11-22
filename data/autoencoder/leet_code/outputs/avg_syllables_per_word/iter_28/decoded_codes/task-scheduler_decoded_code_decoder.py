from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapify(max_heap)

        time = 0
        queue = []

        while max_heap or queue:
            # Release tasks from cooldown if their cooldown has expired
            while queue and queue[0][0] == time:
                _, count = queue.pop(0)
                if count < 0:
                    heappush(max_heap, count)

            if max_heap:
                count = heappop(max_heap) + 1  # Increment count because it's negative
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
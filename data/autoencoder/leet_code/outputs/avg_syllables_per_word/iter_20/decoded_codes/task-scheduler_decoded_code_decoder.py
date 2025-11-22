from collections import Counter
from heapq import heappush, heappop, heapify
from typing import List, Tuple

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap: List[int] = [-count for count in task_counts.values()]
        heapify(max_heap)

        time = 0
        queue: List[Tuple[int, int]] = []

        while max_heap or queue:
            # Release tasks from cooldown whose cooldown time is up
            while queue and queue[0][0] == time:
                _, count = queue.pop(0)
                if count < 0:
                    heappush(max_heap, count)

            if max_heap:
                count = heappop(max_heap) + 1  # Increment count since stored as negative
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
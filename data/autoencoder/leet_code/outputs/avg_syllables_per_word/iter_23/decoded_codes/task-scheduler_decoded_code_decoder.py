from collections import Counter
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = []
        for count in task_counts.values():
            heapq.heappush(max_heap, -count)

        time = 0
        queue = []  # Elements are tuples of (ready_time, count)

        while max_heap or queue:
            # Release tasks whose cooldown ended
            while queue and queue[0][0] == time:
                _, count = queue.pop(0)
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # one instance of this task executed
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
from collections import Counter, deque
from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapify(max_heap)

        time = 0
        queue = deque()  # store tuples of (available_time, count)

        while max_heap or queue:
            # Reinsert tasks whose cooldown has finished
            while queue and queue[0][0] == time:
                _, count = queue.popleft()
                if count < 0:
                    heappush(max_heap, count)

            if max_heap:
                count = heappop(max_heap) + 1  # execute task, decrement count
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
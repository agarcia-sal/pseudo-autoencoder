from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # will hold pairs of (available_time, count)

        while max_heap or queue:
            while queue and queue[0][0] == time:
                _, count = queue.popleft()
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # one occurrence processed
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # stores pairs of (ready_time, count)

        while max_heap or queue:
            # Release tasks whose cooldown has expired at current time
            while queue and queue[0][0] == time:
                _, count = queue.popleft()
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap) + 1  # increment count towards zero
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
import heapq
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = []  # pairs of (time_ready, count)

        while max_heap or queue:
            # Release tasks from cooldown if their time_ready equals current time
            while queue and queue[0][0] == time:
                time_ready, count = queue.pop(0)
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # increment towards zero since counts are negative
                if count < 0:
                    queue.append((time + n + 1, count))
            time += 1

            # Keep queue sorted by time_ready as we appended new elements to the end
            # For efficiency, maintain queue as a heap or sorted structure
            # But since n and tasks size are small, sorting here is fine
            queue.sort(key=lambda x: x[0])

        return time
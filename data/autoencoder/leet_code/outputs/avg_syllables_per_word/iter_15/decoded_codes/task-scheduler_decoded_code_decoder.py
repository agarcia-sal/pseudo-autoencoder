import heapq
from collections import Counter
from typing import List, Tuple

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue: List[Tuple[int, int]] = []

        while max_heap or queue:
            # release tasks whose cooldown has finished
            while queue and queue[0][0] == time:
                _, count = queue.pop(0)
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # increment because counts are negative
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
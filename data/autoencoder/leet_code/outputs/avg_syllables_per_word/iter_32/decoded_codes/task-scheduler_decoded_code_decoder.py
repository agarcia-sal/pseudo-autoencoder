import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequencies of each task
        task_counts = Counter(tasks)

        # Create a max heap by pushing negative counts
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        # Queue to hold pairs of (next_available_time, count)
        queue = deque()

        time = 0

        while max_heap or queue:
            # Release tasks whose cooldown has finished
            while queue and queue[0][0] == time:
                _, count = queue.popleft()
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Increment count since it's negative
                if count < 0:
                    # Append with next available time after cooldown
                    queue.append((time + n + 1, count))

            time += 1

        return time
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time_counter = 0
        queue = deque()  # holds pairs of (ready_time, count)

        while max_heap or queue:
            # Release tasks whose cooldown has expired
            while queue and queue[0][0] == time_counter:
                ready_time, count = queue.popleft()
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # increment towards zero since count is negative
                if count < 0:
                    queue.append((time_counter + n + 1, count))

            time_counter += 1

        return time_counter
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # stores tuples of (time_when_available, count)

        while max_heap or queue:
            # Release tasks from cooldown if their time has come
            while queue and queue[0][0] == time:
                _, count = queue.popleft()
                if count < 0:
                    heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # decrement count since count is negative
                if count < 0:
                    queue.append((time + n + 1, count))

            time += 1

        return time
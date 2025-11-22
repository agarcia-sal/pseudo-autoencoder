from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, task_list: list[str], cooldown_interval: int) -> int:
        task_counts = Counter(task_list)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # holds tuples of (time_to_release, count_value)

        while max_heap or queue:
            # Release tasks from cooldown if their release time is now
            while queue and queue[0][0] == time:
                _, count_value = queue.popleft()
                if count_value < 0:
                    heapq.heappush(max_heap, count_value)

            if max_heap:
                count_value = heapq.heappop(max_heap) + 1  # run a task (decrement its count)
                if count_value < 0:
                    queue.append((time + cooldown_interval + 1, count_value))

            time += 1

        return time
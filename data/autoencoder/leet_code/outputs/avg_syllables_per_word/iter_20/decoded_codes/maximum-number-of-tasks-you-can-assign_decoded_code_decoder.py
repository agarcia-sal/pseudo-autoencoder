from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:]
            pills_used = 0
            # We will use a list to represent available_workers and remove assigned workers by index.
            # Because we need efficient bisect and removals, use list + bisect + del.

            # Copy the list so modifications don't affect original workers list.
            available_workers = available_workers.copy()

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    del available_workers[idx]
                else:
                    if pills_used < pills:
                        idx = bisect_left(available_workers, task - strength)
                        if idx < len(available_workers):
                            del available_workers[idx]
                            pills_used += 1
                        else:
                            return False
                    else:
                        return False
            return True

        left, right = 0, min(len(tasks), len(workers)) + 1
        while left < right:
            mid = (left + right) // 2
            if canAssignTasks(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
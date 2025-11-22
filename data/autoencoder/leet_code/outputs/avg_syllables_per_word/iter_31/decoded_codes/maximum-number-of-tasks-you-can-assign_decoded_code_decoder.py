from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:]
            pills_used = 0

            # We'll keep available_workers sorted as we remove elements.
            # Using a list and bisect for searching.
            # Removing an element at index is O(k), but k <= len(tasks) <= 10^5 should be okay.
            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    available_workers.pop(idx)
                else:
                    if pills_used == pills:
                        return False
                    # Using a pill, find worker >= task - strength
                    idx = bisect_left(available_workers, task - strength)
                    if idx == len(available_workers):
                        return False
                    available_workers.pop(idx)
                    pills_used += 1
            return True

        left, right = 0, min(len(tasks), len(workers)) + 1
        while left < right:
            mid = (left + right) // 2
            if canAssignTasks(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
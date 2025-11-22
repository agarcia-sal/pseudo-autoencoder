from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:]  # last k workers (strongest)
            pills_used = 0
            # Use a list so we can remove elements; will maintain sorted order.
            # Since we only remove elements by index, using list is okay here.
            available = available_workers.copy()

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                # Try to find worker with skill >= task without pill
                idx = bisect_left(available, task)
                if idx < len(available):
                    # assign this worker without pill
                    del available[idx]
                else:
                    # try to assign pill
                    if pills_used < pills:
                        # find worker with skill >= task - strength (since pill adds strength)
                        idx_pill = bisect_left(available, task - strength)
                        if idx_pill < len(available):
                            del available[idx_pill]
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
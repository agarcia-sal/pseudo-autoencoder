from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:]
            pills_used = 0
            # Using a list and manual removal; for efficiency, maintain the list sorted, use bisect.
            # Since we remove elements often, convert to a list to allow removal by index.
            # To keep efficiency, use a list since k <= len(workers) and max 10^5 (acceptable).
            # Removal by index O(k), total O(k^2), but with constraints and 5 seconds likely acceptable.
            # Alternatively, use a balanced tree structure, but not needed here.

            for task_idx in range(k - 1, -1, -1):
                task = tasks[task_idx]
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    del available_workers[idx]
                elif pills_used < pills:
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
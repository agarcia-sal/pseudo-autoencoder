from typing import List
import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:]
            pills_used = 0
            # Use a sorted list to maintain available_workers for efficient removals
            import bisect
            available_workers_list = available_workers.copy()

            for i in range(k - 1, -1, -1):
                task = tasks[i]

                # Find smallest worker >= task
                idx = bisect.bisect_left(available_workers_list, task)
                if idx < len(available_workers_list):
                    available_workers_list.pop(idx)
                else:
                    # Try to use a pill
                    if pills_used < pills:
                        idx = bisect.bisect_left(available_workers_list, task - strength)
                        if idx < len(available_workers_list):
                            available_workers_list.pop(idx)
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
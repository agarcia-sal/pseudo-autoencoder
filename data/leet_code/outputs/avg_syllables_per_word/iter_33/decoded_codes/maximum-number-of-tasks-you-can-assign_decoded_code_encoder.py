import bisect

class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:].copy()
            pills_used = 0
            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect.bisect_left(available_workers, task)
                if idx < len(available_workers):
                    # Assign worker who can do task without pill
                    available_workers.pop(idx)
                else:
                    if pills_used < pills:
                        # Try to assign worker who can do task with pill
                        idx = bisect.bisect_left(available_workers, task - strength)
                        if idx < len(available_workers):
                            available_workers.pop(idx)
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
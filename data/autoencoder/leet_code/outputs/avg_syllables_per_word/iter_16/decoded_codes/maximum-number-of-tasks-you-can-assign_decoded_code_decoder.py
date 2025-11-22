from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:]
            pills_used = 0
            # Use a list as a multiset to track available workers for efficient removals
            # Insert removal operation by index. Since removing from middle may be O(k),
            # but k <= len(tasks)/len(workers), this is acceptable.
            for idx in range(k - 1, -1, -1):
                task = tasks[idx]
                pos = bisect_left(available_workers, task)
                if pos < len(available_workers):
                    available_workers.pop(pos)
                else:
                    if pills_used == pills:
                        return False
                    pos = bisect_left(available_workers, task - strength)
                    if pos < len(available_workers):
                        available_workers.pop(pos)
                        pills_used += 1
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
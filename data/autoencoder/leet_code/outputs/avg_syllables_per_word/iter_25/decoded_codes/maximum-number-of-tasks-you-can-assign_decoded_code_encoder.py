from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def canAssignTasks(k):
            available_workers = workers[-k:]  # last k workers
            pills_used = 0

            # We'll manage available_workers as a sorted list to remove workers efficiently.
            # Convert to list to allow removal by index.
            available_workers = list(available_workers)

            for i in range(k - 1, -1, -1):
                task = tasks[i]

                # Find leftmost worker who can do the task without pill
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    # Assign this worker; remove from available_workers
                    available_workers.pop(idx)
                else:
                    # Try to assign worker with pill: look for worker with strength >= task - strength
                    if pills_used == pills:
                        return False
                    needed = task - strength
                    idx = bisect_left(available_workers, needed)
                    if idx == len(available_workers):
                        return False
                    pills_used += 1
                    available_workers.pop(idx)
            return True

        left, right = 0, min(len(tasks), len(workers)) + 1
        while left < right:
            mid = (left + right) // 2
            if canAssignTasks(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
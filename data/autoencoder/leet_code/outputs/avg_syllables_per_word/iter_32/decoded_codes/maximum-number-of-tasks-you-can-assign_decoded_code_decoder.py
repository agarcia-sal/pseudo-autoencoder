from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k) -> bool:
            # Use a copy of the last k workers since we assign tasks starting from hardest to easiest
            available_workers = workers[-k:]
            pills_used = 0

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                # Find worker who can do task without pill
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    # Assign this worker and remove from list
                    available_workers.pop(idx)
                else:
                    if pills_used >= pills:
                        return False
                    # Need a worker who can do task with pill (worker strength + strength >= task)
                    # So find worker with strength >= task - strength
                    required_strength = task - strength
                    idx = bisect_left(available_workers, required_strength)
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
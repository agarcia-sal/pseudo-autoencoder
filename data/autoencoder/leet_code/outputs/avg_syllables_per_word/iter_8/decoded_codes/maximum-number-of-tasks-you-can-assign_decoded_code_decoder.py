from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def canAssignTasks(k):
            available_workers = workers[-k:]
            pills_used = 0

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                worker_idx = bisect_left(available_workers, task)
                if worker_idx < len(available_workers):
                    del available_workers[worker_idx]
                else:
                    if pills_used < pills:
                        worker_idx = bisect_left(available_workers, task - strength)
                        if worker_idx < len(available_workers):
                            del available_workers[worker_idx]
                            pills_used += 1
                        else:
                            return False
                    else:
                        return False
            return True

        left = 0
        right = min(len(tasks), len(workers)) + 1

        while left < right:
            mid = (left + right) // 2
            if canAssignTasks(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def canAssignTasks(k):
            available = workers[-k:]
            pills_used = 0
            # Work from hardest task to easiest
            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(available, task)
                if idx < len(available):
                    del available[idx]
                else:
                    if pills_used == pills:
                        return False
                    idx = bisect_left(available, task - strength)
                    if idx == len(available):
                        return False
                    del available[idx]
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
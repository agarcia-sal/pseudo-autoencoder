import bisect

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def canAssignTasks(k):
            available = workers[-k:]
            pills_used = 0

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect.bisect_left(available, task)
                if idx < len(available):
                    available.pop(idx)
                elif pills_used < pills:
                    idx = bisect.bisect_left(available, task - strength)
                    if idx < len(available):
                        available.pop(idx)
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
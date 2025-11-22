from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def canAssignTasks(k):
            available_workers = workers[-k:]  # last k workers
            pills_used = 0

            # Using a list to simulate a multiset with bisect operations
            # Note: We'll modify available_workers in place, so copy it
            available_workers = available_workers[:]

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    # Worker can complete task without pill
                    available_workers.pop(idx)
                else:
                    if pills_used < pills:
                        # Try assigning pill: worker strength must be at least task - strength
                        idx = bisect_left(available_workers, task - strength)
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
from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def canAssignTasks(k):
            # Take the k strongest workers (last k elements)
            available_workers = workers[-k:]
            pills_used = 0

            from collections import deque
            available_workers = deque(available_workers)  # will convert back to list each iteration or use list directly

            # Because we remove arbitrary elements, use a list and maintain sorted order
            # So better to keep available_workers as a list and use bisect operations.
            # But after removal, list shrinks, so need to be careful.
            # Let's just keep it as a list.

            available_workers = list(available_workers)

            # Iterate tasks in descending order (largest tasks first)
            for i in range(k - 1, -1, -1):
                task = tasks[i]

                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    # Assign worker without pill
                    available_workers.pop(idx)
                else:
                    # Try using a pill
                    if pills_used < pills:
                        adjusted_task = task - strength
                        idx = bisect_left(available_workers, adjusted_task)
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
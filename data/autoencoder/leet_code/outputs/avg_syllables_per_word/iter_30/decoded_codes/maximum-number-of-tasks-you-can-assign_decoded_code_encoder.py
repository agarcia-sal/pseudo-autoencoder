from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def canAssignTasks(k):
            available_workers = workers[-k:]  # last k workers
            pills_used = 0
            # Use a sorted list for efficient removals and bisect
            from bisect import bisect_left

            # Convert to list for removals; as available_workers is sorted ascending:
            # we will be removing elements via pop(idx)
            # Since k can be large, and removals in list are O(k) worst case,
            # a better data structure is recommended (e.g., SortedList via external libs)
            # but since standard libs only allowed, we use list + bisect

            available = available_workers.copy()

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(available, task)
                if idx < len(available):
                    # Assign worker who can do task without pills
                    available.pop(idx)
                elif pills_used < pills:
                    # Try to assign worker who can do task with pill (worker >= task - strength)
                    idx = bisect_left(available, task - strength)
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
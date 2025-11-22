from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[len(workers) - k:]
            pills_used = 0
            # Use a list to simulate removal, but to optimize,
            # store available_workers as a list and perform bisect searches.
            # Since k can be large, it's more efficient to use a balanced data structure.
            # However, as per constraints, using list + bisect + pop is acceptable.
            # We'll manage available_workers as a sorted list.
            # Since we remove elements by index, use del to remove them.
            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    del available_workers[idx]
                else:
                    if pills_used == pills:
                        return False
                    # search for worker who can do task with pill (task - strength)
                    idx = bisect_left(available_workers, task - strength)
                    if idx == len(available_workers):
                        return False
                    del available_workers[idx]
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
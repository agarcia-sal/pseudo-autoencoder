from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[-k:]
            pills_used = 0
            # Use a list to maintain sorted available_workers for bisect operations
            # As we remove elements, we keep the list sorted
            from bisect import bisect_left
            import collections

            # Using a list as the available_workers is already sorted
            # but we need efficient removal from arbitrary positions
            # Using list and pop by index is O(k), but since k is at most len(workers), acceptable here.

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(available_workers, task)
                if idx < len(available_workers):
                    del available_workers[idx]
                else:
                    if pills_used < pills:
                        idx = bisect_left(available_workers, task - strength)
                        if idx < len(available_workers):
                            del available_workers[idx]
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
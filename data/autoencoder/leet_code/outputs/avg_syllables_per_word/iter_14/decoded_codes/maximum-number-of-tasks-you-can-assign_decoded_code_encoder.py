from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssignTasks(k: int) -> bool:
            available_workers = workers[len(workers) - k:]
            pills_used = 0

            # Since we need efficient removals, we simulate with a list but remove by index carefully.
            # To avoid repeatedly removing from the middle of list, we'll use a balanced structure.
            # However, given constraints and for clarity, we will implement using bisect and removing with pop.
            # Because available_workers is sorted, repeated removals from anywhere in the list are expensive (O(k)),
            # but since k ≤ len(tasks) and within reasonable constraints, this is acceptable here.

            # To optimize, we'll use a list and simulate removals via a linked balanced tree,
            # but for clarity, we implement straightforwardly with list and bisect.

            # To improve removal efficiency, convert to a collections.deque is not helpful as removals are arbitrary.
            # Use a list, but removals from middle O(k) per removal.
            # For better efficiency, we can use a SortedList from sortedcontainers if allowed.

            # Since the prompt allows standard modules, we will import and use SortedList for clarity and efficiency.
            # However, since sortedcontainers is not in standard library, we'll implement a simplified version.
            # Instead, we convert available_workers into a list and do removal using pop.
            # We'll reverse iterate and remove the used workers to minimize removal cost if possible.

            # But the best is to use a balanced BST like structure removed from standard library -> no.
            # We will implement with a list and pop at index, which can be accepted given constraints.

            from bisect import bisect_left
            aw = available_workers.copy()  # Copy to not affect original workers list

            for i in range(k - 1, -1, -1):
                task = tasks[i]
                idx = bisect_left(aw, task)
                if idx < len(aw):
                    aw.pop(idx)
                else:
                    if pills_used < pills:
                        idx = bisect_left(aw, task - strength)
                        if idx < len(aw):
                            aw.pop(idx)
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
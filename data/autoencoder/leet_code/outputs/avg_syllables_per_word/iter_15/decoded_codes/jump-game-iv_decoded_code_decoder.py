from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        value_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_indices[val].append(i)

        queue = deque([(0, 0)])
        visited = {0}

        while queue:
            current_index, steps = queue.popleft()

            if current_index == n - 1:
                return steps

            next_indices = [current_index + 1, current_index - 1] + value_indices[arr[current_index]]

            for next_index in next_indices:
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

            value_indices[arr[current_index]].clear()

        return -1
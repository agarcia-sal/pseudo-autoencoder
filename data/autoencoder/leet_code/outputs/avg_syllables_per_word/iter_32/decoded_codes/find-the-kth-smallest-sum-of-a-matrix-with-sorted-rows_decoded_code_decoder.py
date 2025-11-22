import heapq
from typing import List, Tuple

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        if m == 0:
            return -1
        n = len(mat[0])
        if n == 0:
            return -1

        # Initial sum is sum of first element in each row
        initial_indices_tuple = tuple(0 for _ in range(m))
        initial_sum = sum(mat[i][0] for i in range(m))

        min_heap: List[Tuple[int, Tuple[int, ...]]] = [(initial_sum, initial_indices_tuple)]
        visited = {initial_indices_tuple}

        while k > 0:
            current_sum, indices = heapq.heappop(min_heap)
            k -= 1
            if k == 0:
                return current_sum
            for i in range(m):
                if indices[i] + 1 < n:
                    new_indices = list(indices)
                    new_indices[i] += 1
                    new_indices_tuple = tuple(new_indices)
                    if new_indices_tuple not in visited:
                        # Calculate updated sum by adjusting only the changed element
                        new_sum = current_sum - mat[i][indices[i]] + mat[i][new_indices[i]]
                        visited.add(new_indices_tuple)
                        heapq.heappush(min_heap, (new_sum, new_indices_tuple))

        return -1
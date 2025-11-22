import heapq
from typing import List, Tuple, Set

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0]) if mat else 0
        initial_sum = sum(row[0] for row in mat)
        initial_indices = tuple(0 for _ in range(m))
        min_heap: List[Tuple[int, Tuple[int, ...]]] = [(initial_sum, initial_indices)]
        visited: Set[Tuple[int, ...]] = {initial_indices}

        while k > 0:
            current_sum, indices = heapq.heappop(min_heap)
            k -= 1
            if k == 0:
                return current_sum
            for i in range(m):
                if indices[i] + 1 < n:
                    new_indices = list(indices)
                    old_index = new_indices[i]
                    new_indices[i] += 1
                    new_indices_tuple = tuple(new_indices)
                    if new_indices_tuple not in visited:
                        new_sum = current_sum - mat[i][old_index] + mat[i][new_indices[i]]
                        visited.add(new_indices_tuple)
                        heapq.heappush(min_heap, (new_sum, new_indices_tuple))
        return -1
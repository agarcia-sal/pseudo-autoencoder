from heapq import heappush, heappop
from typing import List, Tuple, Set

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        if m == 0:
            return -1
        n = len(mat[0])
        if any(len(row) != n for row in mat):
            return -1  # Inconsistent row lengths

        initial_sum = sum(row[0] for row in mat)
        initial_indices = tuple(0 for _ in range(m))
        min_heap: List[Tuple[int, Tuple[int, ...]]] = [(initial_sum, initial_indices)]
        visited: Set[Tuple[int, ...]] = {initial_indices}

        while k > 0:
            current_sum, indices = heappop(min_heap)
            k -= 1
            if k == 0:
                return current_sum

            for i in range(m):
                if indices[i] + 1 < n:
                    new_indices = list(indices)
                    new_indices[i] += 1
                    new_indices_tuple = tuple(new_indices)
                    if new_indices_tuple not in visited:
                        old_element = mat[i][indices[i]]
                        new_element = mat[i][new_indices[i]]
                        new_sum = current_sum - old_element + new_element
                        visited.add(new_indices_tuple)
                        heappush(min_heap, (new_sum, new_indices_tuple))

        return -1
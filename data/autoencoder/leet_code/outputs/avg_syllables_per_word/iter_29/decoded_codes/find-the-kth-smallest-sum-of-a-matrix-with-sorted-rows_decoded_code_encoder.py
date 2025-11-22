import heapq
from typing import List, Tuple

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0

        # initial_sum is sum of the 0th elements of each row
        initial_sum = sum(row[0] for row in mat)
        initial_indices = tuple(0 for _ in range(m))

        min_heap: List[Tuple[int, Tuple[int, ...]]] = [(initial_sum, initial_indices)]
        visited = {initial_indices}

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
                    # Compute new_sum by replacing old element with new element in row i
                    new_sum = current_sum - mat[i][indices[i]] + mat[i][new_indices[i]]
                    if new_indices_tuple not in visited:
                        visited.add(new_indices_tuple)
                        heapq.heappush(min_heap, (new_sum, new_indices_tuple))

        return -1
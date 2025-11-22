import heapq
from typing import List, Tuple

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        if m == 0:
            return -1
        n = len(mat[0])
        if any(len(row) != n for row in mat):
            # All rows should have the same length
            return -1
        if k <= 0:
            return -1

        # Initial sum: sum of the first elements of each row
        initial_indices = tuple(0 for _ in range(m))
        initial_sum = sum(mat[i][0] for i in range(m))

        min_heap: List[Tuple[int, Tuple[int, ...]]] = [(initial_sum, initial_indices)]
        visited = set([initial_indices])

        while min_heap and k > 0:
            current_sum, indices = heapq.heappop(min_heap)
            k -= 1
            if k == 0:
                return current_sum

            for i in range(m):
                if indices[i] + 1 < n:
                    new_indices_list = list(indices)
                    new_indices_list[i] += 1
                    new_indices_tuple = tuple(new_indices_list)
                    if new_indices_tuple not in visited:
                        new_sum = current_sum - mat[i][indices[i]] + mat[i][new_indices_list[i]]
                        visited.add(new_indices_tuple)
                        heapq.heappush(min_heap, (new_sum, new_indices_tuple))

        return -1
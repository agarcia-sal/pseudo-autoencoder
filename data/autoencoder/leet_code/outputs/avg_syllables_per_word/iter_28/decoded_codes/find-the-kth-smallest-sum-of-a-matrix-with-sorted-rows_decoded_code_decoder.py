import heapq
from typing import List, Tuple

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        if m == 0:
            return -1
        n = len(mat[0])
        if n == 0 or k <= 0:
            return -1

        initial_sum = 0
        for row in mat:
            if not row:
                return -1
            initial_sum += row[0]

        initial_indices = tuple(0 for _ in range(m))
        min_heap: List[Tuple[int, Tuple[int, ...]]] = [(initial_sum, initial_indices)]
        visited = {initial_indices}

        while min_heap and k > 0:
            current_sum, indices = heapq.heappop(min_heap)
            k -= 1
            if k == 0:
                return current_sum

            for i in range(m):
                current_index = indices[i]
                if current_index + 1 < n:
                    new_indices_list = list(indices)
                    new_indices_list[i] = current_index + 1
                    new_indices = tuple(new_indices_list)

                    old_value = mat[i][current_index]
                    new_value = mat[i][current_index + 1]
                    new_sum = current_sum - old_value + new_value

                    if new_indices not in visited:
                        visited.add(new_indices)
                        heapq.heappush(min_heap, (new_sum, new_indices))

        return -1
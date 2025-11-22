from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, mat, k):
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0
        initial_indices = tuple(0 for _ in range(m))
        initial_sum = sum(mat[i][0] for i in range(m))
        min_heap = [(initial_sum, initial_indices)]
        visited = {initial_indices}

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
                    new_sum = current_sum - mat[i][indices[i]] + mat[i][new_indices[i]]
                    if new_indices_tuple not in visited:
                        visited.add(new_indices_tuple)
                        heappush(min_heap, (new_sum, new_indices_tuple))
        return -1
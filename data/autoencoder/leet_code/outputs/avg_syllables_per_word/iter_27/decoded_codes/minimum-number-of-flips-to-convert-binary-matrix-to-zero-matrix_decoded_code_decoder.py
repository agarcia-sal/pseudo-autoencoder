from collections import deque
from copy import deepcopy
from typing import List, Tuple

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def flip(matrix: List[List[int]], x: int, y: int) -> None:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    matrix[nx][ny] = 1 - matrix[nx][ny]

        def matrix_to_tuple(matrix: List[List[int]]) -> Tuple[Tuple[int, ...], ...]:
            return tuple(tuple(row) for row in matrix)

        m = len(mat)
        if m == 0:
            return 0  # Empty matrix requires zero flips
        n = len(mat[0])
        if any(len(row) != n for row in mat):
            return -1  # Irregular matrix rows, invalid input

        target = tuple(tuple(0 for _ in range(n)) for _ in range(m))
        initial_state = matrix_to_tuple(mat)

        if initial_state == target:
            return 0  # Already at target

        queue = deque([(initial_state, 0)])
        visited = {initial_state}

        while queue:
            current_state, steps = queue.popleft()
            if current_state == target:
                return steps

            current_matrix = [list(row) for row in current_state]

            for i in range(m):
                for j in range(n):
                    next_matrix = deepcopy(current_matrix)
                    flip(next_matrix, i, j)
                    next_state = matrix_to_tuple(next_matrix)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))

        return -1
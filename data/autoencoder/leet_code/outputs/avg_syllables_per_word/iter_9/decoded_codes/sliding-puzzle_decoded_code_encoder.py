from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        start = tuple(tuple(row) for row in board)
        target = ((1, 2, 3), (4, 5, 0))
        neighbors = {
            0: {1, 3},
            1: {0, 2, 4},
            2: {1, 5},
            3: {0, 4},
            4: {1, 3, 5},
            5: {2, 4},
        }

        zero_pos = next(i * 3 + j for i in range(2) for j in range(3) if start[i][j] == 0)

        queue = deque([(start, zero_pos, 0)])
        visited = {start}

        while queue:
            state, zero_pos, moves = queue.popleft()
            if state == target:
                return moves

            i, j = divmod(zero_pos, 3)
            for neighbor in neighbors[zero_pos]:
                ni, nj = divmod(neighbor, 3)
                new_state = [list(row) for row in state]
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                new_tuple_state = tuple(tuple(row) for row in new_state)

                if new_tuple_state not in visited:
                    visited.add(new_tuple_state)
                    queue.append((new_tuple_state, neighbor, moves + 1))

        return -1
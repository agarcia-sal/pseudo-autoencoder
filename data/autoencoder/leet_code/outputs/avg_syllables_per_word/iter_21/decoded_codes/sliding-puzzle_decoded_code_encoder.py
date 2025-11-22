from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        start = self.convert_board_to_tuple(board)
        target = self.define_target_state()
        neighbors = self.define_neighbors()

        zero_pos = 0
        for i in range(2):
            for j in range(3):
                if start[i][j] == 0:
                    zero_pos = i * 3 + j

        queue = self.initialize_queue(start, zero_pos, 0)
        visited = self.initialize_visited(start)

        while queue:
            state, zero_pos, moves = queue.popleft()
            if state == target:
                return moves
            for neighbor in neighbors[zero_pos]:
                new_state = self.deep_copy_state(state)
                i, j = divmod(zero_pos, 3)
                ni, nj = divmod(neighbor, 3)
                self.swap_positions(new_state, i, j, ni, nj)
                new_tuple_state = self.convert_state_to_tuple(new_state)
                if new_tuple_state not in visited:
                    visited.add(new_tuple_state)
                    queue.append((new_tuple_state, neighbor, moves + 1))
        return -1

    def convert_board_to_tuple(self, board):
        return tuple(tuple(row) for row in board)

    def define_target_state(self):
        return ((1, 2, 3), (4, 5, 0))

    def define_neighbors(self):
        return {
            0: {1, 3},
            1: {0, 2, 4},
            2: {1, 5},
            3: {0, 4},
            4: {1, 3, 5},
            5: {2, 4}
        }

    def initialize_queue(self, start, zero_pos, moves):
        return deque([(start, zero_pos, moves)])

    def initialize_visited(self, start):
        return {start}

    def deep_copy_state(self, state):
        return [list(row) for row in state]

    def swap_positions(self, new_state, i, j, ni, nj):
        new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]

    def convert_state_to_tuple(self, new_state):
        return tuple(tuple(row) for row in new_state)
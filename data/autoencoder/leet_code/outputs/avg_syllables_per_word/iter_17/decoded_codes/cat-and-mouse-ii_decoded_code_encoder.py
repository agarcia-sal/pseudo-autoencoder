from collections import deque
from typing import List, Tuple


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        cat_start_position = 0
        mouse_start_position = 0
        food_position = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        g_mouse = self.initializeGraph(number_of_rows * number_of_columns)
        g_cat = self.initializeGraph(number_of_rows * number_of_columns)

        for row_index, row in enumerate(grid):
            for column_index, character in enumerate(row):
                if character == '#':
                    continue
                vertex = row_index * number_of_columns + column_index
                if character == 'C':
                    cat_start_position = vertex
                elif character == 'M':
                    mouse_start_position = vertex
                elif character == 'F':
                    food_position = vertex

                for a, b in directions:
                    # Mouse moves
                    for k in range(mouseJump + 1):
                        x = row_index + k * a
                        y = column_index + k * b
                        if (
                            x < 0 or x >= number_of_rows or
                            y < 0 or y >= number_of_columns or
                            grid[x][y] == '#'
                        ):
                            break
                        g_mouse[vertex].append(x * number_of_columns + y)
                    # Cat moves
                    for k in range(catJump + 1):
                        x = row_index + k * a
                        y = column_index + k * b
                        if (
                            x < 0 or x >= number_of_rows or
                            y < 0 or y >= number_of_columns or
                            grid[x][y] == '#'
                        ):
                            break
                        g_cat[vertex].append(x * number_of_columns + y)

        result = self.calc(g_mouse, g_cat, mouse_start_position, cat_start_position, food_position)
        return result == 1

    def calc(
        self,
        g_mouse: List[List[int]],
        g_cat: List[List[int]],
        mouse_start: int,
        cat_start: int,
        hole: int
    ) -> int:
        # ans[mouse_position][cat_position][turn] = state_result
        # state_result: 0 = unknown, 1 = mouse wins, 2 = cat wins
        number_of_positions = len(g_mouse)

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            mouse_position, cat_position, turn = state
            previous_turn = turn ^ 1  # xor with 1 switches turn between 0 and 1
            previous_states_list = []
            if previous_turn == 1:
                # previous turn was cat's turn
                for previous_cat_position in g_cat[cat_position]:
                    if ans[mouse_position][previous_cat_position][1] == 0:
                        previous_states_list.append((mouse_position, previous_cat_position, previous_turn))
            else:
                # previous turn was mouse's turn
                for previous_mouse_position in g_mouse[mouse_position]:
                    if ans[previous_mouse_position][cat_position][0] == 0:
                        previous_states_list.append((previous_mouse_position, cat_position, previous_turn))
            return previous_states_list

        # degree[mouse][cat][turn][0 or 1] stores the number of next states for the current state.
        degree = self.initializeThreeDimensionalList(number_of_positions, number_of_positions)
        for i in range(number_of_positions):
            for j in range(number_of_positions):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = self.initializeThreeDimensionalList(number_of_positions, number_of_positions)
        queue = self.initializeDeque()

        # Initialize terminal states:
        # If cat and mouse are at the hole or cat and mouse are at the same position, the result is decided immediately.
        for i in range(number_of_positions):
            # mouse at hole: mouse wins
            ans[hole][i][1] = 1  # cat's turn mouse wins
            # cat at hole: cat wins
            ans[i][hole][0] = 2  # mouse's turn cat wins
            # mouse meets cat: cat wins
            ans[i][i][0] = 2
            ans[i][i][1] = 2
            queue.append((hole, i, 1))
            queue.append((i, hole, 0))
            queue.append((i, i, 0))
            queue.append((i, i, 1))

        while queue:
            state = queue.popleft()
            mouse_position, cat_position, turn = state
            current_turn_result = ans[mouse_position][cat_position][turn]
            for previous_state in get_prev_states(state):
                previous_mouse, previous_cat, previous_turn = previous_state
                if previous_turn == current_turn_result - 1:
                    # The current player can force a win:
                    if ans[previous_mouse][previous_cat][previous_turn] == 0:
                        ans[previous_mouse][previous_cat][previous_turn] = current_turn_result
                        queue.append(previous_state)
                else:
                    degree[previous_mouse][previous_cat][previous_turn] -= 1
                    if degree[previous_mouse][previous_cat][previous_turn] == 0:
                        # No moves left for player to avoid losing:
                        if ans[previous_mouse][previous_cat][previous_turn] == 0:
                            ans[previous_mouse][previous_cat][previous_turn] = current_turn_result
                            queue.append(previous_state)

        return ans[mouse_start][cat_start][0]

    def initializeGraph(self, size: int) -> List[List[int]]:
        return [[] for _ in range(size)]

    def initializeThreeDimensionalList(self, dim1_size: int, dim2_size: int) -> List[List[List[int]]]:
        # Returns list of dim1_size x dim2_size x 2 integers initialized to 0
        return [[[0, 0] for _ in range(dim2_size)] for _ in range(dim1_size)]

    def initializeDeque(self) -> deque:
        return deque()
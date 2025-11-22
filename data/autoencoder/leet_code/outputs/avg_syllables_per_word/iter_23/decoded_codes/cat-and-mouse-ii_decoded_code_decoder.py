from collections import deque
from typing import List, Tuple

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        total_rows = len(grid)
        total_columns = len(grid[0]) if total_rows > 0 else 0
        cat_start_position = 0
        mouse_start_position = 0
        food_position = 0
        directions = [-1, 0, 1, 0, -1]

        total_positions = total_rows * total_columns
        mouse_graph = [[] for _ in range(total_positions)]
        cat_graph = [[] for _ in range(total_positions)]

        # Precompute adjacency lists for mouse and cat moves
        for row_index, row_string in enumerate(grid):
            for column_index, character in enumerate(row_string):
                if character == '#':  # Wall
                    continue
                current_position = row_index * total_columns + column_index
                if character == 'C':
                    cat_start_position = current_position
                elif character == 'M':
                    mouse_start_position = current_position
                elif character == 'F':
                    food_position = current_position

                # Directions: adjacent in 4 directions and staying in place (step_index=0)
                for d in range(4):
                    direction_a = directions[d]
                    direction_b = directions[d + 1]

                    # Mouse moves
                    for step_index in range(mouseJump + 1):
                        next_x = row_index + step_index * direction_a
                        next_y = column_index + step_index * direction_b
                        if (next_x < 0 or next_x >= total_rows or
                            next_y < 0 or next_y >= total_columns or
                            grid[next_x][next_y] == '#'):
                            break
                        mouse_graph[current_position].append(next_x * total_columns + next_y)

                    # Cat moves
                    for step_index in range(catJump + 1):
                        next_x = row_index + step_index * direction_a
                        next_y = column_index + step_index * direction_b
                        if (next_x < 0 or next_x >= total_rows or
                            next_y < 0 or next_y >= total_columns or
                            grid[next_x][next_y] == '#'):
                            break
                        cat_graph[current_position].append(next_x * total_columns + next_y)

        # Invoke the calculation function with initial parameters
        return self.calc(mouse_graph, cat_graph, mouse_start_position, cat_start_position, food_position) == 1

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int, cat_start: int, hole: int) -> int:
        total_positions = len(g_mouse)

        # answer[mouse_position][cat_position][turn] = 0(not decided), 1(win for mouse), 2(win for cat)
        answer = [[[0, 0] for _ in range(total_positions)] for __ in range(total_positions)]
        # degree[mouse_position][cat_position][turn] = number of next moves available in this turn
        degrees = [[[0, 0] for _ in range(total_positions)] for __ in range(total_positions)]

        for mouse_pos in range(total_positions):
            for cat_pos in range(total_positions):
                degrees[mouse_pos][cat_pos][0] = len(g_mouse[mouse_pos])
                degrees[mouse_pos][cat_pos][1] = len(g_cat[cat_pos])

        queue = deque()

        # Terminal conditions initialization
        for pos in range(total_positions):
            # If mouse is at the hole, mouse wins immediately on mouse turn
            answer[hole][pos][1] = 1  # mouse turn = 1
            queue.append((hole, pos, 1))
            # If cat is at the hole, cat wins immediately on mouse turn
            answer[pos][hole][0] = 2  # mouse turn = 0
            queue.append((pos, hole, 0))
            # If cat catches mouse, cat wins immediately
            answer[pos][pos][0] = 2
            queue.append((pos, pos, 0))
            answer[pos][pos][1] = 2
            queue.append((pos, pos, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            mouse_position, cat_position, turn = state
            previous_turn = turn ^ 1
            previous_states = []
            if previous_turn == 1:
                # Previous turn was mouse's turn, so cat just moved
                for prev_cat_position in g_cat[cat_position]:
                    if answer[mouse_position][prev_cat_position][1] == 0:
                        previous_states.append((mouse_position, prev_cat_position, 1))
            else:
                # Previous turn was cat's turn, so mouse just moved
                for prev_mouse_position in g_mouse[mouse_position]:
                    if answer[prev_mouse_position][cat_position][0] == 0:
                        previous_states.append((prev_mouse_position, cat_position, 0))
            return previous_states

        # BFS to propagate the results backwards
        while queue:
            current_state = queue.popleft()
            mouse_pos, cat_pos, turn = current_state
            current_result = answer[mouse_pos][cat_pos][turn]
            for prev_mouse, prev_cat, prev_turn in get_prev_states(current_state):
                if prev_turn == current_result - 1:
                    # If previous player can win by moving to current_state
                    if answer[prev_mouse][prev_cat][prev_turn] == 0:
                        answer[prev_mouse][prev_cat][prev_turn] = current_result
                        queue.append((prev_mouse, prev_cat, prev_turn))
                else:
                    degrees[prev_mouse][prev_cat][prev_turn] -= 1
                    if degrees[prev_mouse][prev_cat][prev_turn] == 0:
                        if answer[prev_mouse][prev_cat][prev_turn] == 0:
                            answer[prev_mouse][prev_cat][prev_turn] = current_result
                            queue.append((prev_mouse, prev_cat, prev_turn))

        return answer[mouse_start][cat_start][0]
from collections import deque
from typing import List, Tuple

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        cat_start = 0
        mouse_start = 0
        food = 0
        dirs = [-1, 0, 1, 0, -1]

        # Graphs: index = position in grid flattened (i * n + j)
        # Each element: list of reachable positions for mouse and cat respectively
        g_mouse = [[] for _ in range(m * n)]
        g_cat = [[] for _ in range(m * n)]

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '#':
                    continue
                v = i * n + j
                if c == 'C':
                    cat_start = v
                elif c == 'M':
                    mouse_start = v
                elif c == 'F':
                    food = v

                # For mouse moves
                for d in range(4):
                    a, b = dirs[d], dirs[d + 1]
                    # Mouse moves
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # Cat moves
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]],
             mouse_start: int, cat_start: int, hole: int) -> int:

        n = len(g_mouse)
        # ans[m][c][t]: state result with mouse at m, cat at c, turn t (0:mouse,1:cat)
        # 0 = unknown, 1 = mouse can win, 2 = cat can win
        ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # degree[m][c][t]: number of next moves for current player in state
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for m_idx in range(n):
            for c_idx in range(n):
                degree[m_idx][c_idx][0] = len(g_mouse[m_idx])       # mouse moves turn
                degree[m_idx][c_idx][1] = len(g_cat[c_idx])         # cat moves turn

        # Helper function to get previous states from a given state
        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m, c, t = state
            pt = t ^ 1  # previous turn
            pre = []
            if pt == 1:  # cat's turn was previous, so cat moved to c
                for pc in g_cat[c]:
                    if ans[m][pc][1] == 0:
                        pre.append((m, pc, pt))
            else:        # mouse's turn was previous, so mouse moved to m
                for pm in g_mouse[m]:
                    if ans[pm][c][0] == 0:
                        pre.append((pm, c, pt))
            return pre

        q = deque()

        # Initialize terminal states:
        # If either mouse or cat is on the food (hole) position,
        # or mouse and cat in the same position (cat wins)
        # These states have immediate results; they seed BFS
        for i in range(n):
            # Cat at hole: mouse turn -> mouse lost
            ans[hole][i][1] = 1  # mouse wins if cat on food on cat's turn
            ans[i][hole][0] = 2  # cat wins if mouse on food on mouse's turn
            # Mouse and cat on same position
            ans[i][i][0] = 2  # cat wins if mouse turn and positions same
            ans[i][i][1] = 2  # cat wins if cat turn and positions same

            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        while q:
            state = q.popleft()
            m_, c_, t_ = state
            t_res = ans[m_][c_][t_]
            for pm, pc, pt in get_prev_states(state):
                if ans[pm][pc][pt] != 0:
                    continue
                if pt == t_res - 1:
                    # Previous player can force a win
                    ans[pm][pc][pt] = t_res
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        # Previous player must lose
                        ans[pm][pc][pt] = t_res
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
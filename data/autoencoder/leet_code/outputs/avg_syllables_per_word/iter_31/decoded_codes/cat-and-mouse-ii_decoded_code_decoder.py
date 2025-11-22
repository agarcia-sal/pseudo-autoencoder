from collections import deque
from typing import List, Tuple

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        cat_start = mouse_start = food = 0
        dirs = [-1, 0, 1, 0, -1]
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

                for a, b in zip(dirs, dirs[1:]):
                    # Mouse moves
                    for k in range(mouseJump + 1):
                        x, y = i + k * a, j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # Cat moves
                    for k in range(catJump + 1):
                        x, y = i + k * a, j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int, cat_start: int, hole: int) -> int:
        n = len(g_mouse)

        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]
        q = deque()

        # Initialize terminal states:
        # When mouse is at hole, mouse wins (state=1)
        # When cat is at hole or cat catches mouse (same pos), mouse loses (state=2)
        for i in range(n):
            ans[hole][i][1] = 1  # mouse at hole, cat anywhere, cat's turn => mouse wins
            ans[i][hole][0] = 2  # mouse anywhere, cat at hole, mouse's turn => mouse loses
            ans[i][i][0] = 2     # mouse caught by cat (same pos), mouse's turn => mouse loses
            ans[i][i][1] = 2     # mouse caught by cat (same pos), cat's turn => mouse loses

            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            prev_turn = t ^ 1
            prev_states = []
            if prev_turn == 1:
                # previous turn was cat's turn
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        prev_states.append((m_pos, pc, 1))
            else:
                # previous turn was mouse's turn
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        prev_states.append((pm, c_pos, 0))
            return prev_states

        while q:
            state = q.popleft()
            m_pos, c_pos, t = state
            t_state = ans[m_pos][c_pos][t]

            for pm, pc, pt in get_prev_states(state):
                if pt == t_state - 1:
                    # If the prev state player can force current player to lose next turn
                    if ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t_state
                        q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0 and ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t_state
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
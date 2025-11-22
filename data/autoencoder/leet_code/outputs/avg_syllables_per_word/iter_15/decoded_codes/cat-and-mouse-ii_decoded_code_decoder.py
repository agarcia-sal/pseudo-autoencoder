from collections import deque
from typing import List, Tuple

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        cat_start = 0
        mouse_start = 0
        food = 0
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

                for d in range(4):
                    a, b = dirs[d], dirs[d+1]
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

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int, cat_start: int, hole: int) -> int:
        n = len(g_mouse)

        # degree[m][c] = [mouse_move_count, cat_move_count]
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        # ans[m][c] = [mouse_state, cat_state]
        # 0 = unknown, 1 = mouse win, 2 = cat win
        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]

        q = deque()

        for i in range(n):
            # If mouse reaches hole, mouse wins, cat turn (1)
            ans[hole][i][1] = 1
            # If cat reaches hole, cat wins, mouse turn (0)
            ans[i][hole][0] = 2
            # If mouse and cat are in same position, cat wins, both turns
            ans[i][i][0] = 2
            ans[i][i][1] = 2

            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:  # previous turn was cat
                # cat moved previously, mouse not moved yet
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        pre.append((m_pos, pc, pt))
            else:
                # mouse moved previously, cat not moved yet
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        pre.append((pm, c_pos, pt))
            return pre

        while q:
            state = q.popleft()
            m_pos, c_pos, t = state
            t_state = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states(state):
                if pt == t_state - 1:
                    ans[pm][pc][pt] = t_state
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t_state
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
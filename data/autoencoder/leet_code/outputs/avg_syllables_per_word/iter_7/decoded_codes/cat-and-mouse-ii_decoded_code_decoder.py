from collections import deque
from typing import List, Tuple


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        cat_start = 0
        mouse_start = 0
        food = 0
        dirs = (-1, 0, 1, 0, -1)

        size = m * n
        g_mouse: List[List[int]] = [[] for _ in range(size)]
        g_cat: List[List[int]] = [[] for _ in range(size)]

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
                    a, b = dirs[d], dirs[d + 1]
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n and grid[x][y] != '#'):
                            break
                        g_mouse[v].append(x * n + y)
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n and grid[x][y] != '#'):
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food == 1)

    def calc(
        self,
        g_mouse: List[List[int]],
        g_cat: List[List[int]],
        mouse_start: int,
        cat_start: int,
        hole: bool,
    ) -> bool:
        n = len(g_mouse)
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque()

        for i in range(n):
            ans[hole][i][1] = 1
            ans[i][hole][0] = 2
            ans[i][i][1] = 2
            ans[i][i][0] = 2
            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_, c_, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                for pc in g_cat[c_]:
                    if ans[m_][pc][1] == 0:
                        pre.append((m_, pc, pt))
            else:
                for pm in g_mouse[m_]:
                    if ans[pm][c_][0] == 0:
                        pre.append((pm, c_, 0))
            return pre

        while q:
            state = q.popleft()
            m_, c_, t = state
            t_val = ans[m_][c_][t]
            for pm, pc, pt in get_prev_states(state):
                if pt == t_val - 1:
                    ans[pm][pc][pt] = t_val
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t_val
                        q.append((pm, pc, pt))
        return ans[mouse_start][cat_start][0] == 1
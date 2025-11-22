from collections import deque
from typing import List, Tuple

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        cat_start = mouse_start = food = 0
        dirs = [-1, 0, 1, 0, -1]
        size = m * n
        g_mouse = [[] for _ in range(size)]
        g_cat = [[] for _ in range(size)]

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
                    # Mouse moves
                    for k in range(mouseJump + 1):
                        x, y = i + k * a, j + k * b
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                        if k != 0 and grid[x][y] == '#':
                            # theoretically will break above, so redundant here, kept consistent
                            break
                    # Cat moves
                    for k in range(catJump + 1):
                        x, y = i + k * a, j + k * b
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)
                        if k != 0 and grid[x][y] == '#':
                            break

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(
        self,
        g_mouse: List[List[int]],
        g_cat: List[List[int]],
        mouse_start: int,
        cat_start: int,
        hole: int,
    ) -> int:
        n = len(g_mouse)

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                # Previous turn cat moves
                for pc in g_cat[c_pos]:
                    if ans[pc][m_pos][1] == 0:
                        pre.append((pc, c_pos, pt))
            else:
                # Previous turn mouse moves
                for pm in g_mouse[m_pos]:
                    if ans[c_pos][pm][0] == 0:
                        pre.append((m_pos, pm, pt))
            return pre

        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]
        q = deque()

        for i in range(n):
            ans[hole][i][1] = 1
            ans[i][hole][0] = 2
            ans[i][i][0] = 2
            ans[i][i][1] = 2
            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        while q:
            m_pos, c_pos, t = q.popleft()
            t_val = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states((m_pos, c_pos, t)):
                if pt == t_val - 1:
                    ans[pm][pc][pt] = t_val
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t_val
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
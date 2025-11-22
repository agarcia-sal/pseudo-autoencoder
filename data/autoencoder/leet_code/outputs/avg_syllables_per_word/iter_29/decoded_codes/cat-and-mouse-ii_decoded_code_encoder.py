from collections import deque
from typing import List

class Solution:
    def canMouseWin(self, mouse_grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(mouse_grid)
        n = len(mouse_grid[0])
        cat_start = 0
        mouse_start = 0
        food = 0
        # directions: (-1,0), (0,1), (1,0), (0,-1)
        dirs = (-1, 0, 1, 0, -1)

        g_mouse = [[] for _ in range(m * n)]
        g_cat = [[] for _ in range(m * n)]

        for i, row in enumerate(mouse_grid):
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
                for idx in range(4):
                    a = dirs[idx]
                    b = dirs[idx + 1]
                    # Mouse moves
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n and mouse_grid[x][y] != '#'):
                            break
                        g_mouse[v].append(x * n + y)
                    # Cat moves
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n and mouse_grid[x][y] != '#'):
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int, cat_start: int, hole: int) -> int:
        n = len(g_mouse)

        # degree[m][c][t] = number of remaining moves (degree) for state (mouse=m, cat=c, turn=t)
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        # ans[m][c][t]:
        # 0 = unknown, 1 = mouse wins, 2 = cat wins
        ans = [[[0,0] for _ in range(n)] for _ in range(n)]
        q = deque()

        for i in range(n):
            # if mouse in hole, mouse wins regardless of cat position or turn
            ans[hole][i][1] = 1
            q.append((hole, i, 1))
            # if cat in hole but mouse not, cat wins
            ans[i][hole][0] = 2
            q.append((i, hole, 0))
            # if cat and mouse in the same cell (not hole), cat wins
            ans[i][i][0] = 2
            ans[i][i][1] = 2
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state):
            m, c, t = state
            pt = t ^ 1  # previous turn
            pre = []
            if pt == 1:  # previous turn was cat's
                # cat moved last turn, so mouse stayed
                for pc in g_cat[c]:
                    # Only add states that are not yet determined (ans=0)
                    if ans[m][pc][pt] == 0:
                        pre.append((m, pc, pt))
            else:  # pt == 0, previous turn was mouse's
                # mouse moved last turn, so cat stayed
                for pm in g_mouse[m]:
                    if ans[pm][c][pt] == 0:
                        pre.append((pm, c, pt))
            return pre

        while q:
            state = q.popleft()
            m, c, t = state
            t_val = ans[m][c][t]
            for pm, pc, pt in get_prev_states(state):
                if pt == t_val - 1:
                    # previous state can force current player to win
                    ans[pm][pc][pt] = t_val
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t_val
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
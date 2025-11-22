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
                for d in range(4):
                    a, b = dirs[d], dirs[d + 1]
                    # mouse moves
                    for k in range(mouseJump + 1):
                        x, y = i + k * a, j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # cat moves
                    for k in range(catJump + 1):
                        x, y = i + k * a, j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(
        self,
        g_mouse: List[List[int]],
        g_cat: List[List[int]],
        mouse_start: int,
        cat_start: int,
        hole: int,
    ) -> int:

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m, c, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                # previous turn was cat's turn, so cat moved
                for pc in g_cat[c]:
                    if ans[m][pc][1] == 0:
                        pre.append((m, pc, pt))
            else:
                # previous turn was mouse's turn, so mouse moved
                for pm in g_mouse[m]:
                    if ans[pm][c][0] == 0:
                        pre.append((pm, c, 0))
            return pre

        n = len(g_mouse)
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # degree[m][c][t] = number of next moves available for player t (0=mouse,1=cat)
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque()

        # Initialize terminal states
        for i in range(n):
            # if cat at hole: mouse loses (1)
            ans[hole][i][1] = 1
            q.append((hole, i, 1))
            # if mouse at hole: mouse wins (2)
            ans[i][hole][0] = 2
            q.append((i, hole, 0))
            # if mouse and cat at same position: mouse loses (2)
            ans[i][i][1] = 2
            ans[i][i][0] = 2
            q.append((i, i, 1))
            q.append((i, i, 0))

        while q:
            m_, c_, t = state = q.popleft()
            cur_ans = ans[m_][c_][t]
            for pm, pc, pt in get_prev_states(state):
                if ans[pm][pc][pt] != 0:
                    continue
                if pt == cur_ans - 1:
                    # if current player can force a win next move, prev state is win
                    ans[pm][pc][pt] = cur_ans
                    q.append((pm, pc, pt))
                else:
                    # else reduce degree
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        # no next moves lead to win => lose state
                        ans[pm][pc][pt] = cur_ans
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
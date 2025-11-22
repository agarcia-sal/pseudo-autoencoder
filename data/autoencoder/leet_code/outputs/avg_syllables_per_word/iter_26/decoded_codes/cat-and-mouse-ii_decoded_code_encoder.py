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
                    a, b = dirs[d], dirs[d+1]
                    # mouse moves
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # cat moves
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
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
        hole: int
    ) -> int:

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m, c, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                # It's cat's turn previously, mouse fixed at m
                for pc in g_cat[c]:
                    if ans[m][pc][1] == 0:
                        pre.append((m, pc, pt))
            else:
                # It's mouse's turn previously, cat fixed at c
                for pm in g_mouse[m]:
                    if ans[pm][c][0] == 0:
                        pre.append((pm, c, 0))
            return pre

        n = len(g_mouse)
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]
        q = deque()

        for i in range(n):
            # cat wins if mouse is at hole (food) no matter cat position on cat's turn
            ans[hole][i][1] = 1
            # mouse wins if cat is at hole no matter mouse position on mouse's turn
            ans[i][hole][0] = 2
            # positions where mouse and cat are at the same cell are cat wins (mouse loses)
            ans[i][i][0] = 2
            ans[i][i][1] = 2
            q.append((hole, i, 1))  # cat's turn, mouse at hole
            q.append((i, hole, 0))  # mouse's turn, cat at hole
            q.append((i, i, 0))      # mouse's turn, same cell
            q.append((i, i, 1))      # cat's turn, same cell

        while q:
            state = q.popleft()
            m_pos, c_pos, turn = state
            t = ans[m_pos][c_pos][turn]
            for pm, pc, pt in get_prev_states(state):
                if pt == t - 1:
                    # previous player can force a win
                    if ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t
                        q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0 and ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
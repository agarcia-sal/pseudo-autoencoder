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
                    # For mouse moves
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # For cat moves
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        # hole: food position, return value from calc
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

        # Initialize terminal states
        for i in range(n):
            # Mouse at hole => mouse wins (1) when it's cat's turn
            ans[hole][i][1] = 1
            q.append((hole, i, 1))
            # Cat at hole => cat wins (2) when it's mouse's turn
            ans[i][hole][0] = 2
            q.append((i, hole, 0))
            # Cat and mouse at same cell => cat wins
            ans[i][i][0] = 2
            ans[i][i][1] = 2
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            prev_turn = t ^ 1
            pre = []
            if prev_turn == 1:
                # Previous turn was cat's turn
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        pre.append((m_pos, pc, prev_turn))
            else:
                # Previous turn was mouse's turn
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        pre.append((pm, c_pos, prev_turn))
            return pre

        while q:
            m_pos, c_pos, t = q.popleft()
            state_val = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states((m_pos, c_pos, t)):
                if pt == state_val - 1:
                    # If current state's value is winning for player pt, previous state becomes winning
                    ans[pm][pc][pt] = state_val
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        # All next moves for player pt lead to losing states => this is losing state
                        ans[pm][pc][pt] = state_val
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
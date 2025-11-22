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

        total = m * n
        g_mouse = [[] for _ in range(total)]
        g_cat = [[] for _ in range(total)]

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
                    # For mouse
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n and grid[x][y] != '#'):
                            break
                        g_mouse[v].append(x * n + y)
                    # For cat
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n and grid[x][y] != '#'):
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int,
             cat_start: int, hole: int) -> int:

        n = len(g_mouse)

        # degree[m][c][t]: degree of state (mouse_pos=m, cat_pos=c, turn=t)
        # t = 0: mouse turn, t = 1: cat turn
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for m_pos in range(n):
            for c_pos in range(n):
                degree[m_pos][c_pos][0] = len(g_mouse[m_pos])
                degree[m_pos][c_pos][1] = len(g_cat[c_pos])

        # ans[m][c][t]: 0=unknown, 1=mouse wins, 2=cat wins
        ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque()

        # Initialize states where mouse or cat reaches the hole (food) or mouse and cat at same position
        # According to problem statement (pseudocode), setup:
        # For all positions i:
        #   ans[hole][i][1] = 1 (mouse turn at mouse on hole, cat anywhere) => mouse wins
        #   ans[hole][i][0] = 2 (cat turn, same as above) => cat wins
        #   ans[i][hole][1] = 2 (cat turn, cat on hole) => cat wins
        #   ans[i][hole][0] = 2 (mouse turn, cat on hole) => cat wins
        # Also for positions where mouse and cat at same:
        #   ans[i][i][0] = 2 (mouse turn) => cat wins
        #   ans[i][i][1] = 2 (cat turn) => cat wins

        for i in range(n):
            ans[hole][i][1] = 1
            ans[hole][i][0] = 2
            ans[i][hole][1] = 2
            ans[i][hole][0] = 2
            ans[i][i][0] = 2
            ans[i][i][1] = 2

            q.append((hole, i, 1))
            q.append((hole, i, 0))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                # Previous turn was cat's turn
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        pre.append((m_pos, pc, pt))
            else:
                # Previous turn was mouse's turn
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        pre.append((pm, c_pos, pt))
            return pre

        while q:
            m_pos, c_pos, t = q.popleft()
            cur_state_win = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states((m_pos, c_pos, t)):
                if pt == cur_state_win - 1:
                    # If previous state can guarantee a win on this turn
                    if ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = cur_state_win
                        q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        if ans[pm][pc][pt] == 0:
                            ans[pm][pc][pt] = 3 - cur_state_win  # Opposite party wins
                            q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
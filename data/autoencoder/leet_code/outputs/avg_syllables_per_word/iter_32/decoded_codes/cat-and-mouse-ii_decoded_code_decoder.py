from collections import deque
from typing import List, Tuple


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        cat_start = 0
        mouse_start = 0
        food = 0
        # Directions for movement: up, right, down, left; represented as pairs (a,b)
        dirs = [-1, 0, 1, 0, -1]

        # Graph adjacency lists for mouse and cat moves: for each cell (flattened),
        # store reachable positions
        g_mouse = [[] for _ in range(m * n)]
        g_cat = [[] for _ in range(m * n)]

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '#':  # wall
                    continue
                v = i * n + j
                if c == 'C':
                    cat_start = v
                elif c == 'M':
                    mouse_start = v
                elif c == 'F':
                    food = v
                # For each direction (pair a,b), build reachable states with jumps
                for dir_idx in range(4):
                    a = dirs[dir_idx]
                    b = dirs[dir_idx + 1]
                    # Mouse moves from v in direction (a,b) up to mouseJump
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # Cat moves from v in direction (a,b) up to catJump
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        # Use the helper function calc to determine if mouse can win starting this state
        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(
        self,
        g_mouse: List[List[int]],
        g_cat: List[List[int]],
        mouse_start: int,
        cat_start: int,
        hole: int,
    ) -> int:
        # n is total number of positions (cells)
        n = len(g_mouse)
        # degree[i][j][t]: number of moves for current player at state (mouse=i, cat=j, turn=t)
        # t=0 means mouse to move, t=1 means cat to move
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])  # mouse's moves count
                degree[i][j][1] = len(g_cat[j])    # cat's moves count

        # ans[i][j][t] = 0 (unknown), 1 (mouse wins), 2 (cat wins)
        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]

        q = deque()

        # Initialize terminal states:
        # If mouse is at hole, with cat at any position, mouse wins (1)
        # If cat is at hole OR cat catches mouse (mouse and cat same pos), cat wins (2)
        for i in range(n):
            ans[hole][i][1] = 1  # mouse at hole, cat move next: mouse wins
            ans[i][hole][0] = 2  # cat at hole, mouse move next: cat wins
            ans[i][i][0] = 2     # cat catches mouse, mouse move next: cat wins
            ans[i][i][1] = 2     # cat catches mouse, cat move next: cat wins

            q.append((hole, i, 1))  # mouse wins states
            q.append((i, hole, 0))  # cat wins states
            q.append((i, i, 0))     # cat wins states
            q.append((i, i, 1))     # cat wins states

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_, c_, t_ = state
            pt = t_ ^ 1  # previous turn (opposite player)
            pre = []
            if pt == 1:
                # Previous turn was cat's turn, so mouse stayed fixed m_
                # Cat could have come from any position that can move to c_
                for pc in g_cat[c_]:
                    if ans[m_][pc][pt] == 0:
                        pre.append((m_, pc, pt))
            else:
                # Previous turn was mouse's turn, so cat stayed fixed c_
                # Mouse could have come from any position that can move to m_
                for pm in g_mouse[m_]:
                    if ans[pm][c_][pt] == 0:
                        pre.append((pm, c_, pt))
            return pre

        while q:
            state = q.popleft()
            m_, c_, t_ = state
            t_val = ans[m_][c_][t_]
            for pm, pc, pt in get_prev_states(state):
                if pt == t_val - 1:
                    # If previous player can force a win, update ans and enqueue
                    ans[pm][pc][pt] = t_val
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        # All moves exhausted without winning, opponent wins
                        ans[pm][pc][pt] = t_val
                        q.append((pm, pc, pt))
        return ans[mouse_start][cat_start][0]
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
        # ans state:
        # 0 = unknown, 1 = mouse wins, 2 = cat wins
        ans = [[[0] * 2 for _ in range(n)] for __ in range(n)]
        # degree[i][j][t]:
        # number of next states from (mouse=i, cat=j, turn=t)
        degree = [[[0] * 2 for _ in range(n)] for __ in range(n)]

        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        # Initialize results for terminal states
        q = deque()
        for i in range(n):
            # If mouse at hole, mouse wins regardless of cat pos and turn
            ans[hole][i][1] = 1
            ans[i][hole][0] = 2
            # If mouse and cat at same position, cat wins
            ans[i][i][1] = 2
            ans[i][i][0] = 2

            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            pt = t ^ 1
            res = []
            if pt == 1:
                # previous turn is cat's turn
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        res.append((m_pos, pc, 1))
            else:
                # previous turn is mouse's turn
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        res.append((pm, c_pos, 0))
            return res

        while q:
            state = q.popleft()
            m_pos, c_pos, t = state
            state_result = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states(state):
                if pt == state_result - 1:
                    # If current state's result is mouse wins (1) and pt=0 or
                    # current state's result is cat wins (2) and pt=1, then
                    # previous state can force a win
                    ans[pm][pc][pt] = state_result
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        # No moves left, so losing position for player to move
                        ans[pm][pc][pt] = state_result
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
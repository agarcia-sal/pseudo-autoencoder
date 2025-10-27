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
                    # mouse neighbors reachable with mouseJump
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # cat neighbors reachable with catJump
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
        hole: int,
    ) -> int:
        n = len(g_mouse)

        # ans[m][c][t]: m=mouse pos, c=cat pos, t=turn (0=mouse,1=cat)
        # 0=unknown, 1=mouse can win, 2=cat can win
        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]

        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        q = deque()

        # Initialize terminal states:
        # If cat or mouse is at hole, cat wins or mouse wins as pre-determined by the rules
        for i in range(n):
            # cat at hole, mouse anywhere, cat turn -> cat wins
            ans[hole][i][1] = 1
            q.append((hole, i, 1))
            # mouse at hole, cat anywhere, mouse turn -> mouse wins
            ans[i][hole][0] = 2
            q.append((i, hole, 0))
            # mouse and cat at the same position, cat wins
            ans[i][i][1] = 2
            ans[i][i][0] = 2
            q.append((i, i, 1))
            q.append((i, i, 0))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            prev_turn = 1 - t
            prev_states = []
            if prev_turn == 1:  # cat's turn previously
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        # previous state was mouse pos m_pos, cat pos pc, cat turn
                        prev_states.append((m_pos, pc, prev_turn))
            else:  # mouse's turn previously
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        # previous state was mouse pos pm, cat pos c_pos, mouse turn
                        prev_states.append((pm, c_pos, prev_turn))
            return prev_states

        while q:
            state = q.popleft()
            m_pos, c_pos, t = state
            state_result = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states(state):
                if pt == state_result - 1:
                    ans[pm][pc][pt] = state_result
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = state_result
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
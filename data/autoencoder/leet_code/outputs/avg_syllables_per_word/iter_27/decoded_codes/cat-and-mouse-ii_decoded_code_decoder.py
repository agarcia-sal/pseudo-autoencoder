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
                    a, b = dirs[d], dirs[d+1]

                    # Mouse moves up to mouseJump steps in direction (a,b)
                    for k in range(mouseJump + 1):
                        x = i + a * k
                        y = j + b * k
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)

                    # Cat moves up to catJump steps in direction (a,b)
                    for k in range(catJump + 1):
                        x = i + a * k
                        y = j + b * k
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self,
             g_mouse: List[List[int]],
             g_cat: List[List[int]],
             mouse_start: int,
             cat_start: int,
             hole: int) -> int:
        n = len(g_mouse)
        # ans[i][j][t]: i = mouse pos, j = cat pos, t = turn (0=mouse,1=cat)
        # 0 = unknown, 1 = mouse wins, 2 = cat wins
        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        # degree[i][j][t] is number of next moves from (i,j,t)

        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        q = deque()

        # Initialize terminal states
        for i in range(n):
            # If mouse at hole, mouse immediately wins (t=1 cat's turn)
            ans[hole][i][1] = 1
            q.append((hole, i, 1))
            # If cat at hole, cat immediately wins (t=0 mouse's turn)
            ans[i][hole][0] = 2
            q.append((i, hole, 0))
            # If cat and mouse at same position, cat wins immediately
            ans[i][i][0] = 2
            ans[i][i][1] = 2
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            mpos, cpos, t = state
            prev_turn = t ^ 1
            pre = []
            if prev_turn == 1:  # prev was cat's turn
                # cat moved from some position pc to cpos
                for pc in g_cat[cpos]:
                    if ans[mpos][pc][prev_turn] == 0:
                        pre.append((mpos, pc, prev_turn))
            else:  # prev_turn == 0, mouse's turn
                # mouse moved from some position pm to mpos
                for pm in g_mouse[mpos]:
                    if ans[pm][cpos][prev_turn] == 0:
                        pre.append((pm, cpos, prev_turn))
            return pre

        while q:
            state = q.popleft()
            mpos, cpos, t = state
            state_result = ans[mpos][cpos][t]
            for pm, pc, pt in get_prev_states(state):
                if pt == state_result - 1:
                    # If prev turn is losing for player to move, now winning for current player
                    ans[pm][pc][pt] = state_result
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        # All next moves lose for current player => current player loses
                        ans[pm][pc][pt] = state_result
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
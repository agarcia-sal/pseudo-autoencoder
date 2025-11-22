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
                for k in range(4):
                    a, b = dirs[k], dirs[k+1]
                    # Mouse reachable positions
                    for step in range(mouseJump + 1):
                        x = i + step * a
                        y = j + step * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # Cat reachable positions
                    for step in range(catJump + 1):
                        x = i + step * a
                        y = j + step * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int, cat_start: int, hole: int) -> int:
        n = len(g_mouse)

        # degree[m][c][t]: number of moves available to player t in state (m,c)
        degree = [[[ [0,0] for _ in range(n)] for _ in range(n)] for _ in range(2)]
        # Since the pseudocode suggests degree is a 3D list: degree[m][c][t]
        # where each is a list of two elements [for mouse moves, for cat moves]
        # The original pseudocode built degree as degree[i][j] = [len(g_mouse[i]), len(g_cat[j])],
        # but then nested weirdly. We reconstruct appropriately:

        # To be consistent with the pseudocode:
        # ans[m][c] = [mouse_status, cat_status]
        # degree[m][c] = [mouse_degree, cat_degree]

        # We will re-implement degree and ans properly as ans[m][c][t] and degree[m][c][t].
        # So first rebuild degree and ans as 3D list [m][c][2]
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])    # mouse moves count at state (i,j)
                degree[i][j][1] = len(g_cat[j])      # cat moves count at state (i,j)

        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]

        q = deque()

        # States where mouse or cat is at hole or same cell are terminal
        # Initialize terminal states and push them in queue

        for i in range(n):
            # Mouse at hole: mouse wins (1)
            ans[hole][i][1] = 1  # cat turn at hole state is mouse wins
            ans[i][hole][0] = 1  # mouse turn at hole state is mouse wins
            # Cat at hole: mouse loses (2)
            ans[hole][i][0] = 2
            ans[i][hole][1] = 2
            # Mouse and cat at same position means cat catches mouse => mouse loses (2)
            ans[i][i][0] = 2
            ans[i][i][1] = 2

            q.append((hole, i, 1))  # cat turn at hole (mouse wins)
            q.append((i, hole, 0))  # mouse turn at hole (mouse wins)
            q.append((i, i, 0))     # mouse turn at same cell (mouse loses)
            q.append((i, i, 1))     # cat turn at same cell (mouse loses)

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, t = state
            pt = t ^ 1  # previous turn
            prev = []
            if pt == 1:  # Previous turn is cat's turn, so cat moved to c_pos
                # Find all cat positions that can move to c_pos when mouse at m_pos
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        prev.append((m_pos, pc, 1))
            else:        # Previous turn is mouse's turn, so mouse moved to m_pos
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        prev.append((pm, c_pos, 0))
            return prev

        while q:
            state = q.popleft()
            m_pos, c_pos, t = state
            cur_status = ans[m_pos][c_pos][t]
            pt = t ^ 1
            for pm, pc, pt2 in get_prev_states(state):
                if pt2 != pt:
                    continue
                if ans[pm][pc][pt] != 0:
                    continue
                # pt is the player to move in prev_state
                # If current state is winning for player t, then prev_state is losing for player pt
                # Because player pt will avoid losing moves
                if cur_status == 2 if pt == 0 else 1:
                    ans[pm][pc][pt] = cur_status
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        # No moves left for player pt to avoid losing, so prev_state is winning for the other player
                        ans[pm][pc][pt] = 2 if pt == 0 else 1
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
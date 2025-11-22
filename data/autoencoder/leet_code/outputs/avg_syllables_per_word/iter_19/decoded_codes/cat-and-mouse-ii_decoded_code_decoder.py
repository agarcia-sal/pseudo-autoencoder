from collections import deque
from typing import List, Tuple

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        cat_start = 0
        mouse_start = 0
        food = 0
        dirs = [-1, 0, 1, 0, -1]  # Directions for movement up, right, down, left
        size = m * n

        # Prepare graphs for mouse and cat moves
        g_mouse = [[] for _ in range(size)]
        g_cat = [[] for _ in range(size)]

        # Precompute moves for mouse and cat from each reachable cell
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

                # For each direction, add all reachable positions within jump limits
                for d in range(4):
                    a, b = dirs[d], dirs[d+1]

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

        # Call the solver function, where hole==1 means mouse's turn, 0 means cat's turn is tracked by XOR
        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse: List[List[int]], g_cat: List[List[int]], mouse_start: int, cat_start: int, hole: int) -> int:
        n = len(g_mouse)
        # degree[m][c][t]: number of next options from mouse=m, cat=c, turn=t (t=0 mouse turn, t=1 cat turn)
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(g_mouse[m])
                degree[m][c][1] = len(g_cat[c])

        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]
        q = deque()

        # Initialize known outcome states
        # When mouse or cat is at the food hole, update states accordingly:
        # ans[m][hole][1] = 1 (mouse wins if mouse to play and cat at hole)
        # ans[hole][c][0] = 2 (cat wins if cat to play and mouse at hole)
        # Also if both at same position (cat catches mouse) - cat wins (2)
        for i in range(n):
            # Mouse at hole, cat turn: mouse has won (1)
            ans[i][hole][1] = 1
            # Cat at hole, mouse turn: cat wins (2)
            ans[hole][i][0] = 2
            # Cat catches mouse: when positions equal, both turns cat wins (2)
            ans[i][i][0] = 2
            ans[i][i][1] = 2

            q.append((i, hole, 1))
            q.append((hole, i, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            m_pos, c_pos, turn = state
            prev_turn = turn ^ 1
            prev_states = []
            if prev_turn == 1:
                # Previous turn was cat's turn
                # So cat was at c_pos last turn and mouse unchanged at m_pos
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        prev_states.append((m_pos, pc, 1))
            else:
                # Previous turn was mouse's turn
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        prev_states.append((pm, c_pos, 0))
            return prev_states

        while q:
            m_pos, c_pos, turn = q.popleft()
            t = ans[m_pos][c_pos][turn]

            for pm, pc, pt in get_prev_states((m_pos, c_pos, turn)):
                if pt == t - 1:
                    # If previous player can force current player loss (win for prev player)
                    if ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t
                        q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    # If no options left for previous player, they lose (set ans accordingly)
                    if degree[pm][pc][pt] == 0 and ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
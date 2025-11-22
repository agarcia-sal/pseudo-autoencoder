from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        m = len(grid)
        n = len(grid[0])
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
                # Build mouse moves graph
                for a, b in zip(dirs, dirs[1:]):
                    # Mouse moves (up to mouseJump steps)
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # Cat moves (up to catJump steps)
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse, g_cat, mouse_start, cat_start, hole):
        def get_prev_states(state):
            m, c, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                # Previous turn is cat's turn, find all cat positions leading to current cat pos
                for pc in g_cat[c]:
                    if ans[m][pc][1] == 0:
                        pre.append((m, pc, pt))
            else:
                # Previous turn is mouse's turn, find all mouse positions leading to current mouse pos
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
            ans[hole][i][1] = 1     # mouse lost (cat at food, cat's turn)
            ans[i][hole][0] = 2     # mouse wins (mouse at food, mouse's turn)
            ans[i][i][1] = 2        # mouse wins (cat and mouse in same cell, cat's turn)
            ans[i][i][0] = 2        # mouse wins (cat and mouse in same cell, mouse's turn)
            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        while q:
            m_pos, c_pos, t = q.popleft()
            tval = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states((m_pos, c_pos, t)):
                if pt == tval - 1:
                    if ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = tval
                        q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0 and ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = tval
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
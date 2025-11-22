from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        m, n = len(grid), len(grid[0])
        cat_start = mouse_start = food = 0
        dirs = (-1, 0, 1, 0, -1)
        size = m * n
        g_mouse = [[] for _ in range(size)]
        g_cat = [[] for _ in range(size)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#':
                    continue
                v = i * n + j
                if grid[i][j] == 'C':
                    cat_start = v
                elif grid[i][j] == 'M':
                    mouse_start = v
                elif grid[i][j] == 'F':
                    food = v

                for d in range(4):
                    a, b = dirs[d], dirs[d + 1]
                    for k in range(mouseJump + 1):
                        x, y = i + k * a, j + k * b
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    for k in range(catJump + 1):
                        x, y = i + k * a, j + k * b
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse, g_cat, mouse_start, cat_start, hole):
        n = len(g_mouse)
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]
        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]

        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        q = deque()

        for i in range(n):
            ans[hole][i][1] = 1      # cat at i, mouse at food, cat turn, mouse wins=1 (mouse wins)
            ans[i][hole][0] = 2      # mouse at i, cat at food, mouse turn, cat wins=2 (cat wins)
            ans[i][i][1] = 2         # mouse and cat at same pos, cat wins
            ans[i][i][0] = 2         # mouse and cat at same pos, cat wins

            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        def get_prev_states(state):
            m_pos, c_pos, turn = state
            prev_turn = turn ^ 1
            res = []
            if prev_turn == 1:
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        res.append((m_pos, pc, 1))
            else:
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        res.append((pm, c_pos, 0))
            return res

        while q:
            m_pos, c_pos, turn = state = q.popleft()
            t = ans[m_pos][c_pos][turn]
            for pm, pc, pt in get_prev_states(state):
                if pt == t - 1:
                    if ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t
                        q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0 and ans[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
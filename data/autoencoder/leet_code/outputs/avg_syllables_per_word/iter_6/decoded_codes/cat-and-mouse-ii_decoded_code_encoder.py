from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        m, n = len(grid), len(grid[0])
        cat_start = mouse_start = food = 0
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
                    a, b = dirs[d], dirs[d+1]

                    # Mouse moves
                    for k in range(mouseJump+1):
                        x, y = i + k*a, j + k*b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)

                    # Cat moves
                    for k in range(catJump+1):
                        x, y = i + k*a, j + k*b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        def calc(g_mouse, g_cat, mouse_start, cat_start, hole):
            n = len(g_mouse)
            degree = [[[0, 0] for _ in range(n)] for __ in range(n)]

            for i in range(n):
                for j in range(n):
                    degree[i][j][0] = len(g_mouse[i])
                    degree[i][j][1] = len(g_cat[j])

            ans = [[[0]*2 for _ in range(n)] for __ in range(n)]
            q = deque()

            # Initialize terminal states
            for i in range(n):
                ans[hole][i][1] = 1  # cat in hole: mouse win
                ans[i][hole][0] = 2  # mouse in hole: cat win
                ans[i][i][0] = 2     # mouse caught by cat
                ans[i][i][1] = 2     # mouse caught by cat
                q.append((hole, i, 1))
                q.append((i, hole, 0))
                q.append((i, i, 0))
                q.append((i, i, 1))

            def get_prev_states(state):
                m_pos, c_pos, t = state
                pt = t ^ 1
                pre = []
                if pt == 1:
                    for pc in g_cat[c_pos]:
                        if ans[m_pos][pc][1] == 0:
                            pre.append((m_pos, pc, pt))
                else:
                    for pm in g_mouse[m_pos]:
                        if ans[pm][c_pos][0] == 0:
                            pre.append((pm, c_pos, 0))
                return pre

            while q:
                state = q.popleft()
                m_pos, c_pos, t = state
                t_ans = ans[m_pos][c_pos][t]
                for pm, pc, pt in get_prev_states(state):
                    if pt == t_ans - 1:
                        ans[pm][pc][pt] = t_ans
                        q.append((pm, pc, pt))
                    else:
                        degree[pm][pc][pt] -= 1
                        if degree[pm][pc][pt] == 0:
                            ans[pm][pc][pt] = t_ans
                            q.append((pm, pc, pt))

            return ans[mouse_start][cat_start][0]

        return calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1
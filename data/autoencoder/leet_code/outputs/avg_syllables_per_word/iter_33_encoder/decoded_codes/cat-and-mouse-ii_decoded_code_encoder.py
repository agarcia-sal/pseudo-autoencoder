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
                for idx in range(4):
                    a = dirs[idx]
                    b = dirs[idx+1]
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

    def calc(self, g_mouse, g_cat, mouse_start, cat_start, hole):
        def get_prev_states(state):
            m, c, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                # cat moves on previous turn
                for pc in g_cat[c]:
                    if ans[m][pc][1] == 0:
                        pre.append((m, pc, pt))
            else:
                # mouse moves on previous turn
                for pm in g_mouse[m]:
                    if ans[pm][c][0] == 0:
                        pre.append((pm, c, pt))
            return pre

        n = len(g_mouse)
        # degree[m][c][t]: number of moves from state (m,c,t)
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque()

        # Initialize terminal states
        for i in range(n):
            # If mouse or cat reaches hole (food)
            ans[hole][i][1] = 1  # cat turn: mouse wins
            ans[hole][i][0] = 2  # mouse turn: cat wins
            ans[i][hole][1] = 2  # cat turn: cat wins
            ans[i][hole][0] = 2  # mouse turn: cat wins
            # Mouse caught by cat
            ans[i][i][1] = 2
            ans[i][i][0] = 2
            q.append((hole, i, 1))
            q.append((hole, i, 0))
            q.append((i, hole, 1))
            q.append((i, hole, 0))
            q.append((i, i, 1))
            q.append((i, i, 0))

        while q:
            state = q.popleft()
            m, c, t = state
            t_ans = ans[m][c][t]
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
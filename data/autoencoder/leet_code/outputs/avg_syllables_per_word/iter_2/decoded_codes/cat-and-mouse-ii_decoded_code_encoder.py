from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        m = len(grid)
        n = len(grid[0])
        cat_start = 0
        mouse_start = 0
        food = 0
        dirs = (-1, 0, 1, 0, -1)
        g_mouse = [[] for _ in range(m * n)]
        g_cat = [[] for _ in range(m * n)]

        for i in range(m):
            row = grid[i]
            for j in range(n):
                c = row[j]
                if c == "#":
                    continue
                v = i * n + j
                if c == "C":
                    cat_start = v
                elif c == "M":
                    mouse_start = v
                elif c == "F":
                    food = v
                for d in range(4):
                    a, b = dirs[d], dirs[d+1]
                    # moves for mouse
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "#":
                            break
                        nxt = x * n + y
                        g_mouse[v].append(nxt)
                    # moves for cat
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "#":
                            break
                        nxt = x * n + y
                        g_cat[v].append(nxt)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse, g_cat, mouse_start, cat_start, hole):
        def get_prev_states(state):
            m_pos, c_pos, t = state
            pt = t ^ 1
            pre = []
            if pt == 1:
                # cat's turn before
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][1] == 0:
                        pre.append((m_pos, pc, pt))
            else:
                # mouse's turn before
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][0] == 0:
                        pre.append((pm, c_pos, 0))
            return pre

        n = len(g_mouse)
        degree = [[[0,0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][0] = len(g_mouse[i])
                degree[i][j][1] = len(g_cat[j])

        ans = [[[0,0] for _ in range(n)] for _ in range(n)]
        q = deque()
        for i in range(n):
            ans[hole][i][1] = 1   # cat wins if mouse is at food on cat's turn
            ans[i][hole][0] = 2   # mouse wins if cat is at food on mouse's turn (cat captured) - but from pseudocode it's 2, cat loses
            ans[i][i][1] = 2      # cat and mouse on same cell on cat's turn => cat wins lost
            ans[i][i][0] = 2      # same on mouse's turn

            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))

        while q:
            state = q.popleft()
            t = ans[state[0]][state[1]][state[2]]
            for prev_state in get_prev_states(state):
                pm, pc, pt = prev_state
                # If previous player's turn (pt) results in a forced win or lose based on current:
                if pt == t - 1:
                    ans[pm][pc][pt] = t
                    q.append(prev_state)
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = t
                        q.append(prev_state)
        return ans[mouse_start][cat_start][0]
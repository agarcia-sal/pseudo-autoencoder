from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        m = len(grid)
        n = len(grid[0])
        cat_start = 0
        mouse_start = 0
        food = 0
        dirs = (-1, 0, 1, 0, -1)
        size = m * n
        g_mouse = [[] for _ in range(size)]
        g_cat = [[] for _ in range(size)]

        def in_range(x, y):
            return 0 <= x < m and 0 <= y < n

        for i in range(m):
            row = grid[i]
            for j in range(n):
                c = row[j]
                if c == '#':
                    continue
                v = i * n + j
                if c == 'C':
                    cat_start = v
                elif c == 'M':
                    mouse_start = v
                elif c == 'F':
                    food = v
                # Build mouse and cat graphs from v, using mouseJump and catJump respectively
                for d in range(4):
                    a, b = dirs[d], dirs[d+1]
                    # mouse moves (up to mouseJump steps)
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not in_range(x, y) or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # cat moves (up to catJump steps)
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not in_range(x, y) or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        def calc(g_mouse, g_cat, mouse_start, cat_start, hole):
            n = len(g_mouse)
            degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    degree[i][j][0] = len(g_mouse[i])
                    degree[i][j][1] = len(g_cat[j])

            ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
            q = deque()

            for i in range(n):
                # states where mouse at hole and cat anywhere, cat moves next => mouse wins
                ans[hole][i][1] = 1
                q.append((hole, i, 1))
                # states where cat at hole and mouse anywhere, mouse moves next => cat wins
                ans[i][hole][0] = 2
                q.append((i, hole, 0))
                # states where cat and mouse at same position, mouse moves next => cat wins
                ans[i][i][0] = 2
                q.append((i, i, 0))
                # states where cat and mouse at same position, cat moves next => cat wins
                ans[i][i][1] = 2
                q.append((i, i, 1))

            def get_prev_states(state):
                m_pos, c_pos, turn = state
                prev_turn = turn ^ 1
                pre_states = []
                if prev_turn == 1:
                    # previous turn was cat's turn, so cat just moved
                    for pc in g_cat[c_pos]:
                        if ans[m_pos][pc][1] == 0:
                            pre_states.append((m_pos, pc, 1))
                else:
                    # previous turn was mouse's turn, so mouse just moved
                    for pm in g_mouse[m_pos]:
                        if ans[pm][c_pos][0] == 0:
                            pre_states.append((pm, c_pos, 0))
                return pre_states

            while q:
                state = q.popleft()
                m_pos, c_pos, turn = state
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

        return calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1
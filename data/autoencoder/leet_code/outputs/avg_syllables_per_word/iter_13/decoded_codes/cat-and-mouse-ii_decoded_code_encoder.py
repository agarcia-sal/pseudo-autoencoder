from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        m, n = len(grid), len(grid[0])
        cat_start = mouse_start = food = 0
        dirs = [-1, 0, 1, 0, -1]

        # Initialize adjacency lists for mouse and cat graph
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

                # Directions encoded as pairs in dirs
                for d in range(4):
                    a, b = dirs[d], dirs[d+1]
                    # Mouse moves
                    for k in range(mouseJump + 1):
                        x, y = i + k * a, j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_mouse[v].append(x * n + y)
                    # Cat moves
                    for k in range(catJump + 1):
                        x, y = i + k * a, j + k * b
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#':
                            break
                        g_cat[v].append(x * n + y)

        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(self, g_mouse, g_cat, mouse_start, cat_start, hole):
        n = len(g_mouse)
        # ans[m][c][t]: 0=unknown,1=mouse win,2=cat win; t:0 mouse turn, 1 cat turn
        ans = [[[0, 0] for _ in range(n)] for __ in range(n)]
        # degree[m][c][t]: number of next states from (m,c,t)
        degree = [[[0, 0] for _ in range(n)] for __ in range(n)]

        for m_pos in range(n):
            for c_pos in range(n):
                degree[m_pos][c_pos][0] = len(g_mouse[m_pos])  # mouse turn degree
                degree[m_pos][c_pos][1] = len(g_cat[c_pos])    # cat turn degree

        q = deque()

        # Initialize terminal states:
        # If mouse or cat is at the hole (food)
        for i in range(n):
            # cat turn, mouse at hole => mouse wins
            ans[hole][i][1] = 1
            q.append((hole, i, 1))
            # mouse turn, cat at hole => cat wins
            ans[i][hole][0] = 2
            q.append((i, hole, 0))
            # mouse and cat at same place (except hole) => cat wins
            # for all i, (i,i), mouse turn = cat turn = 2
            if i != hole:
                ans[i][i][0] = 2
                ans[i][i][1] = 2
                q.append((i, i, 0))
                q.append((i, i, 1))

        def get_prev_states(state):
            m_pos, c_pos, t = state
            prev_turn = t ^ 1  # previous turn
            pre = []
            if prev_turn == 1:  # prev turn is cat's turn
                for pc in g_cat[c_pos]:
                    if ans[m_pos][pc][prev_turn] == 0:
                        pre.append((m_pos, pc, prev_turn))
            else:  # prev turn is mouse's turn
                for pm in g_mouse[m_pos]:
                    if ans[pm][c_pos][prev_turn] == 0:
                        pre.append((pm, c_pos, prev_turn))
            return pre

        while q:
            state = q.popleft()
            m_pos, c_pos, t = state
            cur_result = ans[m_pos][c_pos][t]
            for pm, pc, pt in get_prev_states(state):
                if pt == cur_result - 1:
                    ans[pm][pc][pt] = cur_result
                    q.append((pm, pc, pt))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        ans[pm][pc][pt] = cur_result
                        q.append((pm, pc, pt))

        return ans[mouse_start][cat_start][0]
from collections import deque

def cat_mouse_game(grid, mouseJump, catJump):
    m, n = len(grid), len(grid[0])
    dirs = (-1, 0, 1, 0, -1)

    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n

    size = m * n
    g_mouse = [[] for _ in range(size)]
    g_cat = [[] for _ in range(size)]

    cat_start = mouse_start = food = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                continue
            v = i * n + j
            if grid[i][j] == "C":
                cat_start = v
            elif grid[i][j] == "M":
                mouse_start = v
            elif grid[i][j] == "F":
                food = v

            for d in range(4):
                a, b = dirs[d], dirs[d + 1]
                # mouse moves
                for k in range(mouseJump + 1):
                    x, y = i + k * a, j + k * b
                    if not in_bounds(x, y) or grid[x][y] == "#":
                        break
                    g_mouse[v].append(x * n + y)
                # cat moves
                for k in range(catJump + 1):
                    x, y = i + k * a, j + k * b
                    if not in_bounds(x, y) or grid[x][y] == "#":
                        break
                    g_cat[v].append(x * n + y)

    def get_prev_states(m_pos, c_pos, t):
        pt = t ^ 1
        pre = []
        if pt == 1:  # cat's turn before
            for pc in g_cat[c_pos]:
                if ans[m_pos][pc][1] == 0:
                    pre.append((m_pos, pc, pt))
        else:  # mouse's turn before
            for pm in g_mouse[m_pos]:
                if ans[pm][c_pos][0] == 0:
                    pre.append((pm, c_pos, 0))
        return pre

    N = size
    degree = [[[0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            degree[i][j][0] = len(g_mouse[i])
            degree[i][j][1] = len(g_cat[j])

    ans = [[[0, 0] for _ in range(N)] for _ in range(N)]
    q = deque()

    for i in range(N):
        # Mouse wins (1) if mouse at food and cat anywhere (cat moves)
        ans[food][i][1] = 1
        q.append((food, i, 1))
        # Cat wins (2) if cat at food and mouse anywhere (mouse moves)
        ans[i][food][0] = 2
        q.append((i, food, 0))
        # Cat wins if mouse and cat on same cell (mouse moves)
        ans[i][i][0] = 2
        q.append((i, i, 0))
        # Cat wins if mouse and cat on same cell (cat moves)
        ans[i][i][1] = 2
        q.append((i, i, 1))

    while q:
        m_pos, c_pos, t = q.popleft()
        cur_ans = ans[m_pos][c_pos][t]

        for pm, pc, pt in get_prev_states(m_pos, c_pos, t):
            if ans[pm][pc][pt] != 0:
                continue

            # If previous player can force a win by moving to current winning state
            if pt == cur_ans - 1:
                ans[pm][pc][pt] = cur_ans
                q.append((pm, pc, pt))
            else:
                degree[pm][pc][pt] -= 1
                if degree[pm][pc][pt] == 0:
                    # no moves left to avoid losing
                    ans[pm][pc][pt] = cur_ans
                    q.append((pm, pc, pt))

    return ans[mouse_start][cat_start][0] == 1
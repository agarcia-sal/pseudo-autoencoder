from functools import cache

DRAW, M_WIN, C_WIN = 0, 1, 2
n = len(graph)

@cache
def dfs(turn, m_pos, c_pos):
    if turn == 2 * n:
        return DRAW
    if m_pos == 0:
        return M_WIN
    if m_pos == c_pos:
        return C_WIN

    player = "mouse" if turn % 2 == 0 else "cat"

    if player == "mouse":
        res = C_WIN
        for nxt in graph[m_pos]:
            r = dfs(turn + 1, nxt, c_pos)
            if r == M_WIN:
                return M_WIN
            elif r == DRAW:
                res = DRAW
        return res
    else:
        res = M_WIN
        for nxt in graph[c_pos]:
            if nxt == 0:
                continue
            r = dfs(turn + 1, m_pos, nxt)
            if r == C_WIN:
                return C_WIN
            elif r == DRAW:
                res = DRAW
        return res

result = dfs(0, 1, 2)
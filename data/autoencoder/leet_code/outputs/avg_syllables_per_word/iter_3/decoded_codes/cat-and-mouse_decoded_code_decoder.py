from functools import cache

class Solution:
    def catMouseGame(self, graph):
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        n = len(graph)

        @cache
        def dfs(turn, mouse_pos, cat_pos):
            if turn == 2 * n:
                return DRAW
            if mouse_pos == 0:
                return MOUSE_WIN
            if mouse_pos == cat_pos:
                return CAT_WIN

            if turn % 2 == 0:
                result = CAT_WIN
                for nxt in graph[mouse_pos]:
                    next_result = dfs(turn + 1, nxt, cat_pos)
                    if next_result == MOUSE_WIN:
                        return MOUSE_WIN
                    if next_result == DRAW:
                        result = DRAW
                return result
            else:
                result = MOUSE_WIN
                for nxt in graph[cat_pos]:
                    if nxt == 0:
                        continue
                    next_result = dfs(turn + 1, mouse_pos, nxt)
                    if next_result == CAT_WIN:
                        return CAT_WIN
                    if next_result == DRAW:
                        result = DRAW
                return result

        return dfs(0, 1, 2)
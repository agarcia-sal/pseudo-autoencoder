class Solution:
    def catMouseGame(self, graph):
        DRAW = 0
        MOUSE_WIN = 1
        CAT_WIN = 2
        n = len(graph)

        def dfs(turn, mouse_pos, cat_pos):
            if turn == 2 * n:
                return DRAW
            if mouse_pos == 0:
                return MOUSE_WIN
            if mouse_pos == cat_pos:
                return CAT_WIN

            if turn % 2 == 0:
                current_player = "mouse"
            else:
                current_player = "cat"

            if current_player == "mouse":
                result = CAT_WIN
                for next_pos in graph[mouse_pos]:
                    next_result = dfs(turn + 1, next_pos, cat_pos)
                    if next_result == MOUSE_WIN:
                        return MOUSE_WIN
                    elif next_result == DRAW:
                        result = DRAW
                return result
            else:
                result = MOUSE_WIN
                for next_pos in graph[cat_pos]:
                    if next_pos == 0:
                        continue
                    next_result = dfs(turn + 1, mouse_pos, next_pos)
                    if next_result == CAT_WIN:
                        return CAT_WIN
                    elif next_result == DRAW:
                        result = DRAW
                return result

        return dfs(0, 1, 2)
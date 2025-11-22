from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        n = len(graph)

        def dfs(turn: int, mouse_pos: int, cat_pos: int) -> int:
            if turn == 2 * n:
                return DRAW
            if mouse_pos == 0:
                return MOUSE_WIN
            if mouse_pos == cat_pos:
                return CAT_WIN

            current_player = 'mouse' if turn % 2 == 0 else 'cat'

            if current_player == 'mouse':
                result = CAT_WIN
                for next_pos in graph[mouse_pos]:
                    next_result = dfs(turn + 1, next_pos, cat_pos)
                    if next_result == MOUSE_WIN:
                        return MOUSE_WIN
                    if next_result == DRAW:
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
                    if next_result == DRAW:
                        result = DRAW
                return result

        return dfs(0, 1, 2)
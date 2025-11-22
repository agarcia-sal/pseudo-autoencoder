from typing import List, Literal

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        DRAW = 0
        MOUSE_WIN = 1
        CAT_WIN = 2
        n = len(graph)

        # We can memoize results to avoid recomputation
        from functools import lru_cache

        # turn ranges from 0 to 2*n - 1
        # positions: mouse_pos and cat_pos in [0, n-1]
        @lru_cache(None)
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
                    elif next_result == DRAW:
                        result = DRAW
                return result

            else:
                # current_player == 'cat'
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
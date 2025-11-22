from typing import Dict, Tuple

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # Mapping of jumps that require a visited intermediate dot
        jumps: Dict[Tuple[int, int], int] = {
            (1, 3): 2, (3, 1): 2,
            (1, 7): 4, (7, 1): 4,
            (3, 9): 6, (9, 3): 6,
            (7, 9): 8, (9, 7): 8,
            (1, 9): 5, (9, 1): 5,
            (2, 8): 5, (8, 2): 5,
            (3, 7): 5, (7, 3): 5,
            (4, 6): 5, (6, 4): 5,
            (5, 5): 5,  # self jump - no actual effect, but retained per pseudocode
        }

        def countPatternsFromDot(current: int, visited: list[bool], length: int) -> int:
            if length == n:
                return 1
            count = 1 if length >= m else 0
            for next_dot in range(1, 10):
                if not visited[next_dot]:
                    jump = jumps.get((current, next_dot), 0)
                    if jump == 0 or visited[jump]:
                        visited[next_dot] = True
                        count += countPatternsFromDot(next_dot, visited, length + 1)
                        visited[next_dot] = False
            return count

        visited = [False] * 10  # index 0 unused
        result = 0
        for i in range(1, 10):
            visited[i] = True
            result += countPatternsFromDot(i, visited, 1)
            visited[i] = False
        return result
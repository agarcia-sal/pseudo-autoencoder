from typing import Dict, Tuple, Optional, List


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # Mapping pairs (min_dot, max_dot) to the dot that must be visited when jumping over
        jumps: Dict[Tuple[int, int], int] = {
            (1, 3): 2,
            (1, 7): 4,
            (1, 9): 5,
            (2, 8): 5,
            (3, 7): 5,
            (3, 9): 6,
            (4, 6): 5,
            (7, 9): 8,
        }

        # Function to get jump dot, keys always stored as (min, max) for symmetry
        def get_jump(a: int, b: int) -> Optional[int]:
            key = (min(a, b), max(a, b))
            return jumps.get(key, None)

        def countPatternsFromDot(current: int, visited: List[bool], length: int) -> int:
            if length == n:
                return 1
            count = 1 if length >= m else 0

            for next_dot in range(1, 10):
                if not visited[next_dot]:
                    jump = get_jump(current, next_dot)
                    if jump is None or visited[jump]:
                        visited[next_dot] = True
                        count += countPatternsFromDot(next_dot, visited, length + 1)
                        visited[next_dot] = False
            return count

        visited = [False] * 10
        result = 0

        # Symmetry:
        # For dots 1,3,7,9 patterns count is same
        visited[1] = True
        count_corner = countPatternsFromDot(1, visited, 1)
        visited[1] = False

        # For dots 2,4,6,8 patterns count is same
        visited[2] = True
        count_edge = countPatternsFromDot(2, visited, 1)
        visited[2] = False

        # For dot 5 patterns count
        visited[5] = True
        count_center = countPatternsFromDot(5, visited, 1)
        visited[5] = False

        # total = 4 * corners + 4 * edges + center
        return 4 * count_corner + 4 * count_edge + count_center
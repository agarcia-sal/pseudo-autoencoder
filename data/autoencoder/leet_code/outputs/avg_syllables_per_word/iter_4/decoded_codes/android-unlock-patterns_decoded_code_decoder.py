class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        jumps = {
            (1, 3): 2, (3, 1): 2,
            (1, 7): 4, (7, 1): 4,
            (3, 9): 6, (9, 3): 6,
            (7, 9): 8, (9, 7): 8,
            (1, 9): 5, (9, 1): 5,
            (3, 7): 5, (7, 3): 5,
            (4, 6): 5, (6, 4): 5,
            (2, 8): 5, (8, 2): 5,
            (5, 5): 5  # included as per pseudocode, though unused
        }

        def countPatternsFromDot(current: int, visited: list, length: int) -> int:
            if length == n:
                return 1

            count = 1 if length >= m else 0

            for next_dot in range(1, 10):
                if not visited[next_dot]:
                    jump = jumps.get((current, next_dot))
                    if jump is None or visited[jump]:
                        visited[next_dot] = True
                        count += countPatternsFromDot(next_dot, visited, length + 1)
                        visited[next_dot] = False
            return count

        visited = [False] * 10
        result = 0

        # Count patterns starting from corner (1)
        visited[1] = True
        corner_count = countPatternsFromDot(1, visited, 1)
        visited[1] = False

        # Count patterns starting from edge (2)
        visited[2] = True
        edge_count = countPatternsFromDot(2, visited, 1)
        visited[2] = False

        # Count patterns starting from center (5)
        visited[5] = True
        center_count = countPatternsFromDot(5, visited, 1)
        visited[5] = False

        # corners * 4 + edges * 4 + center
        return corner_count * 4 + edge_count * 4 + center_count
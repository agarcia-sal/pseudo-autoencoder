class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # Mapping pairs of dots to the intermediate dot that must be visited between them, if any
        jump_table = {
            (1, 3): 2, (3, 1): 2,
            (1, 7): 4, (7, 1): 4,
            (1, 9): 5, (9, 1): 5,
            (2, 8): 5, (8, 2): 5,
            (3, 7): 5, (7, 3): 5,
            (3, 9): 6, (9, 3): 6,
            (4, 6): 5, (6, 4): 5,
            (7, 9): 8, (9, 7): 8,
            (5, 5): 5  # Though not meaningful, included as per original pseudocode
        }

        def countPatternsFromDot(current_dot: int, visited_map: list[bool], current_length: int) -> int:
            if current_length == n:
                return 1
            count = 1 if current_length >= m else 0
            for next_dot in range(1, 10):
                if not visited_map[next_dot]:
                    required_jump_dot = jump_table.get((current_dot, next_dot))
                    if required_jump_dot is None or visited_map[required_jump_dot]:
                        visited_map[next_dot] = True
                        count += countPatternsFromDot(next_dot, visited_map, current_length + 1)
                        visited_map[next_dot] = False
            return count

        visited_map = [False] * 10  # Index 0 unused; dots numbered 1 through 9
        total_patterns = 0
        for dot_index in range(1, 10):
            visited_map[dot_index] = True
            total_patterns += countPatternsFromDot(dot_index, visited_map, 1)
            visited_map[dot_index] = False
        return total_patterns
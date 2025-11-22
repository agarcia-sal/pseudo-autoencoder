class Solution:
    def findRotateSteps(self, ring, key):
        def create_char_positions(ring):
            char_positions = {}
            for index in range(len(ring)):
                c = ring[index]
                if c not in char_positions:
                    char_positions[c] = []
                char_positions[c].append(index)
            return char_positions

        char_positions = create_char_positions(ring)
        n = len(ring)
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, prev_pos):
            if i == len(key):
                return 0

            min_steps = float('inf')
            for pos in char_positions[key[i]]:
                clockwise = (pos - prev_pos) % n
                anticlockwise = (prev_pos - pos) % n
                steps = min(clockwise, anticlockwise) + 1 + dp(i + 1, pos)
                if steps < min_steps:
                    min_steps = steps

            return min_steps

        return dp(0, 0)
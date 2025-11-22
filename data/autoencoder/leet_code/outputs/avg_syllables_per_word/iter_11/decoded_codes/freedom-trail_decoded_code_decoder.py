from math import inf

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = {}
        for index in range(len(ring)):
            c = ring[index]
            if c not in char_positions:
                char_positions[c] = []
            char_positions[c].append(index)

        n = len(ring)

        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0
            min_steps = inf
            for pos in char_positions[key[i]]:
                clockwise = (pos - prev_pos) % n
                anticlockwise = (prev_pos - pos) % n
                steps = min(clockwise, anticlockwise) + 1 + dp(i + 1, pos)
                if steps < min_steps:
                    min_steps = steps
            return min_steps

        return dp(0, 0)
from collections import defaultdict
from math import inf

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        for i, char in enumerate(ring):
            char_positions[char].append(i)
        n = len(ring)

        from functools import lru_cache

        @lru_cache(None)
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
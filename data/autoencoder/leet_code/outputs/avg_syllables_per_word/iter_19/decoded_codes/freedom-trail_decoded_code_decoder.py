from collections import defaultdict
from math import inf
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring, key):
        char_positions = defaultdict(list)
        n = len(ring)
        for i in range(n):
            char_positions[ring[i]].append(i)

        @lru_cache(None)
        def dp(i, prev_pos):
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
from collections import defaultdict
from math import inf
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        for index in range(len(ring)):
            char_positions[ring[index]].append(index)
        n = len(ring)

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0
            min_steps = inf
            for position in char_positions[key[i]]:
                distance_clockwise = (position - prev_pos) % n
                distance_anticlockwise = (prev_pos - position) % n
                steps = min(distance_clockwise, distance_anticlockwise) + 1 + dp(i + 1, position)
                if steps < min_steps:
                    min_steps = steps
            return min_steps

        return dp(0, 0)
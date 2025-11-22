from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        n = len(ring)
        for index, ch in enumerate(ring):
            char_positions[ch].append(index)

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0
            min_steps = float('inf')
            for position in char_positions[key[i]]:
                clockwise = (position - prev_pos) % n
                anticlockwise = (prev_pos - position) % n
                steps = min(clockwise, anticlockwise) + 1 + dp(i + 1, position)
                min_steps = min(min_steps, steps)
            return min_steps

        return dp(0, 0)
from collections import defaultdict
from math import inf
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        for i, ch in enumerate(ring):
            char_positions[ch].append(i)
        n = len(ring)

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0
            min_steps = inf
            target_char = key[i]
            for pos in char_positions[target_char]:
                clockwise = (pos - prev_pos) % n
                anticlockwise = (prev_pos - pos) % n
                step_count = min(clockwise, anticlockwise) + 1 + dp(i + 1, pos)
                if step_count < min_steps:
                    min_steps = step_count
            return min_steps

        return dp(0, 0)
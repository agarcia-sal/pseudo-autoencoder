from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        char_positions = defaultdict(list)
        for index, ch in enumerate(ring):
            char_positions[ch].append(index)

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0

            min_steps = float('inf')
            current_char = key[i]
            for pos in char_positions[current_char]:
                clockwise = (pos - prev_pos) % n
                anticlockwise = (prev_pos - pos) % n
                step = min(clockwise, anticlockwise) + 1 + dp(i + 1, pos)
                if step < min_steps:
                    min_steps = step
            return min_steps

        return dp(0, 0)
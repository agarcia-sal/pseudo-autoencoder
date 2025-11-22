from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        n = len(ring)
        for i, ch in enumerate(ring):
            char_positions[ch].append(i)

        @lru_cache(None)
        def dp(i, prev_pos):
            if i == len(key):
                return 0
            res = float('inf')
            for pos in char_positions[key[i]]:
                clockwise = (pos - prev_pos) % n
                anticlockwise = (prev_pos - pos) % n
                steps = min(clockwise, anticlockwise) + 1 + dp(i + 1, pos)
                if steps < res:
                    res = steps
            return res

        return dp(0, 0)
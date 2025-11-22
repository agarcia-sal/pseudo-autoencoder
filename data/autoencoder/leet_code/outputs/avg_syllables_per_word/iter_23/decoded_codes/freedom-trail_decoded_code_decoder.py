from collections import defaultdict
import sys

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        for index, ch in enumerate(ring):
            char_positions[ch].append(index)

        n = len(ring)
        sys.setrecursionlimit(10**7)
        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0
            min_steps = float('inf')
            target_char = key[i]
            for position in char_positions[target_char]:
                clockwise = (position - prev_pos) % n
                anticlockwise = (prev_pos - position) % n
                # 1 step for pressing the button after rotation
                steps = min(clockwise, anticlockwise) + 1 + dp(i + 1, position)
                min_steps = min(min_steps, steps)
            return min_steps

        return dp(0, 0)
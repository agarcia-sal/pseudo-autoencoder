from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        for index, ch in enumerate(ring):
            char_positions[ch].append(index)
        n = len(ring)

        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0

            min_steps = float('inf')
            target_char = key[i]
            for pos in char_positions[target_char]:
                # Calculate clockwise and anticlockwise distances
                clockwise = (pos - prev_pos) % n
                anticlockwise = (prev_pos - pos) % n
                step_count = min(clockwise, anticlockwise) + 1 + dp(i + 1, pos)
                if step_count < min_steps:
                    min_steps = step_count
            return min_steps

        return dp(0, 0)
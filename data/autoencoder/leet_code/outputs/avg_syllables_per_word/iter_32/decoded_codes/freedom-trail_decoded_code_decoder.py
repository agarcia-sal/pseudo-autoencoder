from typing import Dict, List
from functools import lru_cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Map each character in 'ring' to all its positions (indices)
        char_positions: Dict[str, List[int]] = {}
        for index, ch in enumerate(ring):
            char_positions.setdefault(ch, []).append(index)

        n = len(ring)

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0  # All characters processed

            min_steps = float('inf')
            # For each occurrence of the current character in ring,
            # calculate the minimal distance to reach it from prev_pos
            for position in char_positions[key[i]]:
                clockwise = (position - prev_pos) % n
                anticlockwise = (prev_pos - position) % n
                distance = clockwise if clockwise < anticlockwise else anticlockwise

                # 1 step for pressing the button + distance to rotate + recursive cost
                steps = distance + 1 + dp(i + 1, position)
                if steps < min_steps:
                    min_steps = steps

            return min_steps

        return dp(0, 0)
from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        for index_position, character_element in enumerate(ring):
            char_positions[character_element].append(index_position)

        n = len(ring)

        @lru_cache(None)
        def dp(i: int, prev_pos: int) -> int:
            if i == len(key):
                return 0

            min_steps = float('inf')
            for position_element in char_positions[key[i]]:
                clockwise_distance = (position_element - prev_pos) % n
                anticlockwise_distance = (prev_pos - position_element) % n
                steps = min(clockwise_distance, anticlockwise_distance) + 1 + dp(i + 1, position_element)
                min_steps = min(min_steps, steps)

            return min_steps

        return dp(0, 0)
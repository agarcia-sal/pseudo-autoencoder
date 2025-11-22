from collections import defaultdict
from math import inf
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = defaultdict(list)
        for index, ch in enumerate(ring):
            char_positions[ch].append(index)
        length_of_ring = len(ring)

        @lru_cache(None)
        def dp(i: int, previous_position: int) -> int:
            if i == len(key):
                return 0

            minimum_steps = inf
            position_list = char_positions[key[i]]
            for position in position_list:
                clockwise_distance = (position - previous_position) % length_of_ring
                anticlockwise_distance = (previous_position - position) % length_of_ring
                steps_to_press = min(clockwise_distance, anticlockwise_distance) + 1
                total_steps = steps_to_press + dp(i + 1, position)
                if total_steps < minimum_steps:
                    minimum_steps = total_steps

            return minimum_steps

        return dp(0, 0)
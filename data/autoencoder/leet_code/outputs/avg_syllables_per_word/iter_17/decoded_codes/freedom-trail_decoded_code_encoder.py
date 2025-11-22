from collections import defaultdict
from functools import lru_cache
import math

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        character_positions = self.create_character_positions_dictionary(ring)
        length_of_ring = len(ring)

        @lru_cache(None)
        def dp(current_index: int, previous_position: int) -> int:
            if current_index == len(key):
                return 0

            minimum_steps = math.inf
            current_char = key[current_index]
            for position in character_positions[current_char]:
                clockwise_distance = (position - previous_position) % length_of_ring
                anticlockwise_distance = (previous_position - position) % length_of_ring
                steps_required = min(clockwise_distance, anticlockwise_distance) + 1 + dp(current_index + 1, position)
                if steps_required < minimum_steps:
                    minimum_steps = steps_required

            return minimum_steps

        return dp(0, 0)

    def create_character_positions_dictionary(self, ring: str) -> defaultdict:
        character_positions = defaultdict(list)
        for index, char in enumerate(ring):
            character_positions[char].append(index)
        return character_positions
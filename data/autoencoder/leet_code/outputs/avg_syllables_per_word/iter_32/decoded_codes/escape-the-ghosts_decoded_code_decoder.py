from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # Player's distance from origin to target (Manhattan distance)
        player_distance = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            # Ghost's Manhattan distance from origin to target
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_distance <= player_distance:
                return False
        return True
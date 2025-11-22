class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        player_distance = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_distance <= player_distance:
                return False
        return True
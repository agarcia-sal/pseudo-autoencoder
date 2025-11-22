from typing import List, Tuple


class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        total_distance = 0
        max_save = float("-inf")

        tree_pos = (tree[0], tree[1])
        squirrel_pos = (squirrel[0], squirrel[1])

        for nut in nuts:
            nut_pos = (nut[0], nut[1])
            dist_tree_nut = distance(nut_pos, tree_pos)
            total_distance += 2 * dist_tree_nut
            dist_squirrel_nut = distance(squirrel_pos, nut_pos)
            save = 2 * dist_tree_nut - (dist_squirrel_nut + dist_tree_nut)
            if save > max_save:
                max_save = save

        return total_distance - max_save
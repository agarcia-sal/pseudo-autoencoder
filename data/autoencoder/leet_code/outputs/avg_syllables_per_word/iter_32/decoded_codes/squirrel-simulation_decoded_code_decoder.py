from typing import List, Tuple
import math

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
            # Manhattan distance between two points
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        total_distance = 0
        max_save = -math.inf

        tree_pt = (tree[0], tree[1])
        squirrel_pt = (squirrel[0], squirrel[1])

        for nut in nuts:
            nut_pt = (nut[0], nut[1])
            dist_tree_nut = distance(nut_pt, tree_pt)
            total_distance += 2 * dist_tree_nut

            first_nut_distance = distance(squirrel_pt, nut_pt) + dist_tree_nut
            later_nut_distance = 2 * dist_tree_nut
            save = later_nut_distance - first_nut_distance
            if save > max_save:
                max_save = save

        return total_distance - max_save
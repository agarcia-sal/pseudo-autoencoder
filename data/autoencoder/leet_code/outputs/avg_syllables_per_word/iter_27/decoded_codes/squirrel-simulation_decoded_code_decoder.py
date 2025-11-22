from typing import List, Tuple

class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: Tuple[int, int],
        squirrel: Tuple[int, int],
        nuts: List[Tuple[int, int]]
    ) -> int:

        def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
            horizontal_difference = abs(p1[0] - p2[0])
            vertical_difference = abs(p1[1] - p2[1])
            total_difference = horizontal_difference + vertical_difference
            return total_difference

        total_distance = 0
        max_save = float('-inf')

        for nut in nuts:
            dist_nut_tree = distance(nut, tree)
            first_nut_distance = distance(squirrel, nut) + dist_nut_tree
            later_nut_distance = dist_nut_tree * 2
            save = later_nut_distance - first_nut_distance

            total_distance += later_nut_distance

            if save > max_save:
                max_save = save

        result = total_distance - max_save
        return result
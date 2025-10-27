class Solution:
    def minDistance(self, height: int, width: int, tree: [int], squirrel: [int], nuts: [[int]]) -> int:
        def distance(p1: [int], p2: [int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        total_distance = 0
        max_save = float('-inf')

        for nut in nuts:
            dist_tree_nut = distance(nut, tree)
            total_distance += 2 * dist_tree_nut
            first_nut_distance = distance(squirrel, nut) + dist_tree_nut
            later_nut_distance = 2 * dist_tree_nut
            save = later_nut_distance - first_nut_distance
            if save > max_save:
                max_save = save

        return total_distance - max_save
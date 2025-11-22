from math import inf

class Solution:
    def minDistance(self, height: int, width: int, tree: [int], squirrel: [int], nuts: [[int]]) -> int:
        def distance(p1: [int], p2: [int]) -> int:
            horizontal_difference = abs(p1[0] - p2[0])
            vertical_difference = abs(p1[1] - p2[1])
            return horizontal_difference + vertical_difference

        total_distance = 0
        max_save = -inf

        for nut in nuts:
            total_distance += 2 * distance(nut, tree)

            first_nut_distance = distance(squirrel, nut) + distance(nut, tree)
            later_nut_distance = 2 * distance(nut, tree)
            save = later_nut_distance - first_nut_distance

            if save > max_save:
                max_save = save

        return total_distance - max_save
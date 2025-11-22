from math import inf

class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def distance(p1, p2):
            horizontal_difference = abs(p1[0] - p2[0])
            vertical_difference = abs(p1[1] - p2[1])
            total_distance = horizontal_difference + vertical_difference
            return total_distance

        total_distance = 0
        max_save = -inf

        for nut in nuts:
            dist_nut_tree = distance(nut, tree)
            total_distance += 2 * dist_nut_tree
            first_nut_distance = distance(squirrel, nut) + dist_nut_tree
            later_nut_distance = 2 * dist_nut_tree
            save = later_nut_distance - first_nut_distance
            if save > max_save:
                max_save = save

        result_distance = total_distance - max_save
        return result_distance
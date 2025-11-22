class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def distance(p1, p2):
            # Manhattan distance
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
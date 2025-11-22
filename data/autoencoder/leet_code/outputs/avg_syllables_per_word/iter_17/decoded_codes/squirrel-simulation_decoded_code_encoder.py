class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def distance(point_one, point_two):
            return abs(point_one[0] - point_two[0]) + abs(point_one[1] - point_two[1])

        total_distance = 0
        max_save = float('-inf')

        for nut in nuts:
            dist_tree_nut = distance(nut, tree)
            total_distance += 2 * dist_tree_nut
            first_nut_distance = distance(squirrel, nut) + dist_tree_nut
            later_nut_distance = 2 * dist_tree_nut
            save = later_nut_distance - first_nut_distance
            max_save = max(max_save, save)

        return total_distance - max_save
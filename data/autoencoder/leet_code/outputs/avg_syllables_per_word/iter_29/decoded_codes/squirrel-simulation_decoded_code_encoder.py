class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def distance(point_one, point_two):
            return abs(point_one[0] - point_two[0]) + abs(point_one[1] - point_two[1])

        total_distance = 0
        max_save = float('-inf')

        for nut in nuts:
            total_distance += 2 * distance(nut, tree)

            first_nut_distance = distance(squirrel, nut) + distance(nut, tree)
            later_nut_distance = 2 * distance(nut, tree)

            save = later_nut_distance - first_nut_distance
            if save > max_save:
                max_save = save

        return total_distance - max_save
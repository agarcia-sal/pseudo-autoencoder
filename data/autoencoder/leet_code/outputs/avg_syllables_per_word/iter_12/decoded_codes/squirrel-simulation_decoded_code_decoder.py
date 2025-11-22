class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def distance(p1, p2):
            horizontal_difference = abs(p1[0] - p2[0])
            vertical_difference = abs(p1[1] - p2[1])
            total_difference = horizontal_difference + vertical_difference
            return total_difference

        total_distance = 0
        max_save = float('-inf')

        for nut in nuts:
            round_trip_distance = distance(nut, tree) * 2
            total_distance += round_trip_distance

            first_nut_distance = distance(squirrel, nut) + distance(nut, tree)
            later_nut_distance = round_trip_distance

            save = later_nut_distance - first_nut_distance
            if save > max_save:
                max_save = save

        result = total_distance - max_save
        return result
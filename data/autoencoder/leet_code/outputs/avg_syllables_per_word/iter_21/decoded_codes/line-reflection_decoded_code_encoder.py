class Solution:
    def isReflected(self, points):
        unique_points = self.convert_list_of_lists_to_set_of_tuples(points)
        min_x = self.find_minimum_x_coordinate(unique_points)
        max_x = self.find_maximum_x_coordinate(unique_points)
        line_of_reflection = (min_x + max_x) / 2
        for point in unique_points:
            x, y = point
            reflected_x = 2 * line_of_reflection - x
            if (reflected_x, y) not in unique_points:
                return False
        return True

    def convert_list_of_lists_to_set_of_tuples(self, points):
        return {tuple(point) for point in points}

    def find_minimum_x_coordinate(self, unique_points):
        minimum_value = float('inf')
        for point in unique_points:
            x = point[0]
            if x < minimum_value:
                minimum_value = x
        return minimum_value

    def find_maximum_x_coordinate(self, unique_points):
        maximum_value = float('-inf')
        for point in unique_points:
            x = point[0]
            if x > maximum_value:
                maximum_value = x
        return maximum_value
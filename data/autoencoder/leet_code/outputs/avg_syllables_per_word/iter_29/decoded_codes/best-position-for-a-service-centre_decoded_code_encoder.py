import math

class Solution:
    def getMinDistSum(self, positions):
        quantity = len(positions)
        x = 0.0
        y = 0.0
        for pair_of_coordinates in positions:
            x_coordinate = pair_of_coordinates[0]
            y_coordinate = pair_of_coordinates[1]
            x += x_coordinate
            y += y_coordinate
        x /= quantity
        y /= quantity

        decay = 0.999
        epsilon = 1e-6
        alpha = 0.5

        while True:
            gradient_x = 0.0
            gradient_y = 0.0
            total_distance = 0.0
            for pair_of_coordinates in positions:
                x_coordinate = pair_of_coordinates[0]
                y_coordinate = pair_of_coordinates[1]
                difference_x = x - x_coordinate
                difference_y = y - y_coordinate
                current_distance = math.sqrt(difference_x * difference_x + difference_y * difference_y)
                # Avoid division by zero by adding a very small number
                gradient_x += difference_x / (current_distance + 1e-7)
                gradient_y += difference_y / (current_distance + 1e-7)
                total_distance += current_distance
            delta_x = gradient_x * alpha
            delta_y = gradient_y * alpha
            x -= delta_x
            y -= delta_y
            alpha *= decay
            if abs(delta_x) <= epsilon and abs(delta_y) <= epsilon:
                return total_distance
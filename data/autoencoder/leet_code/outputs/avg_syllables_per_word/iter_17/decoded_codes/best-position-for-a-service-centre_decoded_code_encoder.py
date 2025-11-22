import math
from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[float]]) -> float:
        n = len(positions)
        x = 0.0
        y = 0.0
        for x1, y1 in positions:
            x += x1
            y += y1
        x /= n
        y /= n

        decay = 0.999
        epsilon = 1e-6
        alpha = 0.5

        while True:
            gradient_x = 0.0
            gradient_y = 0.0
            total_distance = 0.0

            for x1, y1 in positions:
                diff_x = x - x1
                diff_y = y - y1
                distance = math.sqrt(diff_x * diff_x + diff_y * diff_y)
                # Add small offset 1e-7 to denominator preventing division by zero
                gradient_x += diff_x / (distance + 1e-7)
                gradient_y += diff_y / (distance + 1e-7)
                total_distance += distance

            delta_x = gradient_x * alpha
            delta_y = gradient_y * alpha
            x -= delta_x
            y -= delta_y
            alpha *= decay

            if abs(delta_x) <= epsilon and abs(delta_y) <= epsilon:
                return total_distance
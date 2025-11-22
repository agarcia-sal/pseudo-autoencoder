import math
from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[float]]) -> float:
        n = len(positions)
        x = 0.0
        y = 0.0
        for position_x, position_y in positions:
            x += position_x
            y += position_y
        x /= n
        y /= n
        decay = 0.999
        epsilon = 1e-6
        alpha = 0.5

        while True:
            grad_x = 0.0
            grad_y = 0.0
            dist = 0.0
            for position_x, position_y in positions:
                a = x - position_x
                b = y - position_y
                c = math.sqrt(a * a + b * b)
                # add a small constant to denominator to avoid division by zero as in pseudocode
                grad_x += a / (c + 1e-8)
                grad_y += b / (c + 1e-8)
                dist += c
            dx = grad_x * alpha
            dy = grad_y * alpha
            x -= dx
            y -= dy
            alpha *= decay
            if abs(dx) <= epsilon and abs(dy) <= epsilon:
                return dist
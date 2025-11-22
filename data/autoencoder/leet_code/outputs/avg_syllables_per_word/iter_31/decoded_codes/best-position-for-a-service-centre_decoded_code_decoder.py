import math

class Solution:
    def getMinDistSum(self, positions):
        n = len(positions)
        x = 0.0
        y = 0.0
        for x1, y1 in positions:
            x += x1
            y += y1
        x /= n
        y /= n

        decay = 0.95
        eps = 1e-7
        alpha = 0.5
        small = 1e-20  # to avoid division by zero

        while True:
            grad_x = 0.0
            grad_y = 0.0
            dist = 0.0
            for x1, y1 in positions:
                a = x - x1
                b = y - y1
                c = math.sqrt(a * a + b * b)
                denom = c + small
                grad_x += a / denom
                grad_y += b / denom
                dist += c
            dx = grad_x * alpha
            dy = grad_y * alpha
            x -= dx
            y -= dy
            alpha *= decay
            if abs(dx) <= eps and abs(dy) <= eps:
                return dist
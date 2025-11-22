import math

class Solution:
    def getMinDistSum(self, positions):
        n = len(positions)
        x = 0.0
        y = 0.0
        for position in positions:
            x1, y1 = position
            x += x1
            y += y1
        x /= n
        y /= n

        decay = 0.999
        eps = 1e-6
        alpha = 0.5

        while True:
            grad_x = 0.0
            grad_y = 0.0
            dist = 0.0
            for position in positions:
                x1, y1 = position
                a = x - x1
                b = y - y1
                c = math.sqrt(a*a + b*b)
                # add small epsilon (1e-8) to denominator to avoid division by zero
                denom = c + 1e-8
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
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

        decay = 0.999
        eps = 1e-5
        alpha = 0.5

        while True:
            grad_x = 0.0
            grad_y = 0.0
            dist = 0.0

            for x1, y1 in positions:
                a = x - x1
                b = y - y1
                c = math.sqrt(a*a + b*b)
                # add small epsilon to denominator to avoid div by zero
                grad_x += a / (c + 1e-7)
                grad_y += b / (c + 1e-7)
                dist += c

            dx = grad_x * alpha
            dy = grad_y * alpha
            x -= dx
            y -= dy
            alpha *= decay

            if abs(dx) <= eps and abs(dy) <= eps:
                return dist
import math

class Solution:
    def getMinDistSum(self, positions):
        n = len(positions)
        x = sum(p[0] for p in positions) / n
        y = sum(p[1] for p in positions) / n
        decay = 0.999
        eps = 1e-6
        alpha = 0.5

        while True:
            grad_x = 0
            grad_y = 0
            dist = 0
            for x1, y1 in positions:
                a = x - x1
                b = y - y1
                c = math.sqrt(a * a + b * b)
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
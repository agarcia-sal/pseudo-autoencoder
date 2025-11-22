from math import sqrt

class Solution:
    def getMinDistSum(self, positions):
        n = len(positions)
        x = sum(p[0] for p in positions) / n
        y = sum(p[1] for p in positions) / n

        decay = 0.999
        eps = 1e-6
        alpha = 0.5

        while True:
            grad_x = grad_y = dist = 0
            for x1, y1 in positions:
                a = x - x1
                b = y - y1
                c = sqrt(a*a + b*b)
                denom = c + 1e-7
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
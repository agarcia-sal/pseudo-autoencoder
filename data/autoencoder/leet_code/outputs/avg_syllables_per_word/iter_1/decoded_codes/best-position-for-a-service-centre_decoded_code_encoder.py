import math

def optimize_position(pos):
    n = len(pos)
    x = sum(p[0] for p in pos) / n
    y = sum(p[1] for p in pos) / n

    decay = 0.999
    eps = 1e-6
    alpha = 0.5

    while True:
        grad_x = 0
        grad_y = 0
        dist = 0
        for (x1, y1) in pos:
            a = x - x1
            b = y - y1
            c = math.sqrt(a*a + b*b)
            grad_x += a / (c + 1e-8)
            grad_y += b / (c + 1e-8)
            dist += c

        dx = grad_x * alpha
        dy = grad_y * alpha

        x -= dx
        y -= dy

        alpha *= decay

        if abs(dx) <= eps and abs(dy) <= eps:
            return dist
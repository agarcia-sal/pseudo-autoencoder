from collections import deque
from math import inf

def max_value(points, k):
    max_val = -inf
    dq = deque()

    for xj, yj in points:
        while dq and xj - dq[0][1] > k:
            dq.popleft()
        if dq:
            max_val = max(max_val, yj + xj + dq[0][0])
        while dq and yj - xj >= dq[-1][0]:
            dq.pop()
        dq.append((yj - xj, xj))

    return max_val
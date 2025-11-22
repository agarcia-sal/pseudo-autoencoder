from collections import deque
from math import inf

class Solution:
    def findMaxValueOfEquation(self, points, k):
        max_value = -inf
        dq = deque()

        for xj, yj in points:
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            if dq:
                max_value = max(max_value, yj + xj + dq[0][0])

            while dq and (yj - xj) >= dq[-1][0]:
                dq.pop()

            dq.append((yj - xj, xj))

        return max_value
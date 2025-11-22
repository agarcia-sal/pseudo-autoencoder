from collections import deque
from math import inf

class Solution:
    def findMaxValueOfEquation(self, points, k):
        max_value = -inf
        deque_ = deque()

        for xj, yj in points:
            # Remove points from deque front if they are out of the k range
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            if deque_:
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Maintain deque in decreasing order of (y - x)
            while deque_ and yj - xj >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
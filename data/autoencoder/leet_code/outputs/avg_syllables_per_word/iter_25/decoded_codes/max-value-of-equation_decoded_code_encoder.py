from collections import deque
from math import inf

class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        max_value = -inf
        deque_ = deque()  # stores pairs (y[i]-x[i], x[i])
        for xj, yj in points:
            # Remove points from deque_ where xj - x[i] > k
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()
            if deque_:
                max_value = max(max_value, yj + xj + deque_[0][0])
            # Maintain deque_ in decreasing order of (y[i]-x[i])
            while deque_ and yj - xj >= deque_[-1][0]:
                deque_.pop()
            deque_.append((yj - xj, xj))
        return max_value
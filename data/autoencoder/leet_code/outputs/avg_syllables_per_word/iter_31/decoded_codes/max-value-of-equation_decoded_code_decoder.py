from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        deque_ = deque()  # stores pairs (y - x, x)

        for xj, yj in points:
            # Remove elements where xj - xi > k
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            if deque_:
                # max_value = max(max_value, yi + yj + abs(xj - xi))
                # Given that the deque stores (yi - xi, xi),
                # the equation becomes: yj + xj + max(yi - xi)
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Maintain deque_ in decreasing order of (y - x)
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        deque_ = deque()  # stores pairs of (y_i - x_i, x_i)

        for xj, yj in points:
            # Remove points from deque front where xj - x_i > k
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            # Update max_value if deque is not empty
            if deque_:
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Maintain deque in decreasing order of (y_i - x_i)
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
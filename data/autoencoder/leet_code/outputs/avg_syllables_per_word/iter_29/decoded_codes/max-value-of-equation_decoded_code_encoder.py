from collections import deque
from math import inf
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = -inf
        deque_ = deque()

        for point in points:
            xj, yj = point

            # Remove points from deque if they are out of the k range with current xj
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            if deque_:
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Maintain deque in decreasing order of (y - x)
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
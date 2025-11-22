from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        deque_ = deque()  # stores pairs (y - x, x)

        for xj, yj in points:
            # Remove elements from front if xj - x > k
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            if deque_:
                # Compute candidate value using max (yi + yj + |xi - xj|)
                # Given the transformation, max_value candidate is yj + xj + max of (yi - xi)
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Maintain deque decreasing by (y - x)
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()
            deque_.append((yj - xj, xj))

        return max_value
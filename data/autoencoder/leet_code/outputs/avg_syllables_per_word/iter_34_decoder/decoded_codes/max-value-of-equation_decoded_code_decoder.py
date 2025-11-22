from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        deque_ = deque()  # stores pairs of (y - x, x)

        for xj, yj in points:
            # Remove elements from the front if xj - x_i > k
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            if deque_:
                # max_value = max(max_value, yj + xj + (y_i - x_i))
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Remove from back while current (y - x) >= last stored (y - x)
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
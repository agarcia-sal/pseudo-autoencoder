from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float("-inf")
        deque_ = deque()  # will store pairs (y - x, x)

        for xj, yj in points:
            # Remove elements from the front if their x is out of range (> k difference)
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            if deque_:
                # Calculate candidate max using current yj, xj and max (y_i - x_i) from deque front
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Remove elements from the back if current (y_j - x_j) is greater or equal
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        deque_ = deque()  # stores tuples of (y_j - x_j, x_j)

        for xj, yj in points:
            # Remove points from the front where xj - x_i > k, i.e., out of range
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            # Update max_value if deque_ not empty
            if deque_:
                # max_value candidate: (y_j + x_j) + (y_i - x_i)
                # == (y_j + x_j) + first element's first tuple value
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Maintain deque_ to keep only potentially optimal candidates:
            # Remove from the end while current (y_j - x_j) >= last element's (y_i - x_i)
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
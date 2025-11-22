from collections import deque
from typing import List, Tuple

class Solution:
    def findMaxValueOfEquation(self, points: List[Tuple[int, int]], k: int) -> int:
        max_value = float('-inf')
        deque_ = deque()  # Will store pairs of (y_i - x_i, x_i) maintaining max y_i - x_i

        for xj, yj in points:
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()
            if deque_:
                max_value = max(max_value, yj + xj + deque_[0][0])
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()
            deque_.append((yj - xj, xj))

        return max_value
from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        deque_ = deque()

        for xj, yj in points:
            # Remove points from the front if their x-coordinate difference with xj is greater than k
            while deque_ and xj - deque_[0][1] > k:
                deque_.popleft()

            if deque_:
                # Update max_value with current candidate
                max_value = max(max_value, yj + xj + deque_[0][0])

            # Maintain deque in decreasing order of (y - x)
            while deque_ and (yj - xj) >= deque_[-1][0]:
                deque_.pop()

            deque_.append((yj - xj, xj))

        return max_value
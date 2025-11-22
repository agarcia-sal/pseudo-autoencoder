from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        dq = deque()

        for xj, yj in points:
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            if dq:
                max_value = max(max_value, yj + xj + dq[0][0])

            while dq and (yj - xj) >= dq[-1][0]:
                dq.pop()

            dq.append((yj - xj, xj))

        return max_value
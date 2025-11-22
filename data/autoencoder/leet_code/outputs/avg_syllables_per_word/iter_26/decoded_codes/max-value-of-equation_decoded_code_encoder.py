from collections import deque
from math import inf
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        maximum_value = -inf
        dq = deque()

        for xj, yj in points:
            # Remove points from the deque that are out of the xj - x constraint (greater than k)
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            if dq:
                # dq[0][0] is (yi - xi), dq[0][1] is xi
                maximum_value = max(maximum_value, yj + xj + dq[0][0])

            # Remove points with smaller (yi - xi) value since current (yj - xj) is better or equal
            while dq and (yj - xj) >= dq[-1][0]:
                dq.pop()

            dq.append((yj - xj, xj))

        return maximum_value
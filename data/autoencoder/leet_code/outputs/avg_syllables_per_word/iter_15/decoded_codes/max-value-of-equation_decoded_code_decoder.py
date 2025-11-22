from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        dq = deque()  # will store pairs (y - x, x)

        for xj, yj in points:
            # Remove points from the front if their x is too far from xj
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            if dq:
                # Calculate candidate value using the front element of deque
                max_value = max(max_value, yj + xj + dq[0][0])

            # Maintain deque to keep the pairs with the greatest (y - x)
            while dq and yj - xj >= dq[-1][0]:
                dq.pop()

            dq.append((yj - xj, xj))

        return max_value
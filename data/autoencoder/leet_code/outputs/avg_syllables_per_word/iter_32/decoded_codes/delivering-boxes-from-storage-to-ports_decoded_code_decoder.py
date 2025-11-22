from math import inf
from typing import List, Tuple

class Solution:
    def boxDelivering(self, boxes: List[Tuple[int, int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        dp = [inf] * (n + 1)
        dp[0] = 0

        left = 0
        current_weight = 0
        extra_trips = 0

        for right in range(n):
            # Add weight of the current box
            current_weight += boxes[right][1]

            # If this box's port is different from the previous box's port, increase extra trips
            if right > 0 and boxes[right][0] != boxes[right - 1][0]:
                extra_trips += 1

            # Shrink the sliding window if limits exceeded (maxBoxes or maxWeight)
            while left <= right and (right - left + 1 > maxBoxes or current_weight > maxWeight):
                current_weight -= boxes[left][1]
                if left > 0 and boxes[left][0] != boxes[left - 1][0]:
                    extra_trips -= 1
                left += 1

            # dp[right+1] = dp[left] + 2 + extra_trips:
            # 2 accounts for departing and returning trips for this delivery range
            dp[right + 1] = dp[left] + 2 + extra_trips

        return dp[n]
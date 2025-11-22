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
            port, weight = boxes[right]
            current_weight += weight

            if right > 0 and port != boxes[right - 1][0]:
                extra_trips += 1

            while left <= right and (right - left + 1 > maxBoxes or current_weight > maxWeight):
                left_port, left_weight = boxes[left]
                current_weight -= left_weight

                if left > 0 and left_port != boxes[left - 1][0]:
                    extra_trips -= 1

                left += 1

            dp[right + 1] = dp[left] + 2 + extra_trips

        return dp[n]
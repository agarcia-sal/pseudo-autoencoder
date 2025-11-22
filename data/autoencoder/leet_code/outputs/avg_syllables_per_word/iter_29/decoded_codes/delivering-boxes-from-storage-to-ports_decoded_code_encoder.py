from math import inf
from typing import List

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        total_number_of_boxes = len(boxes)
        dp = [inf] * (total_number_of_boxes + 1)
        dp[0] = 0

        left_pointer = 0
        current_weight_total = 0
        extra_trips_count = 0

        for right_pointer in range(total_number_of_boxes):
            current_weight_total += boxes[right_pointer][1]
            if right_pointer > 0 and boxes[right_pointer][0] != boxes[right_pointer - 1][0]:
                extra_trips_count += 1

            while left_pointer <= right_pointer and ((right_pointer - left_pointer + 1) > maxBoxes or current_weight_total > maxWeight):
                current_weight_total -= boxes[left_pointer][1]
                if left_pointer > 0 and boxes[left_pointer][0] != boxes[left_pointer - 1][0]:
                    extra_trips_count -= 1
                left_pointer += 1

            dp[right_pointer + 1] = dp[left_pointer] + 2 + extra_trips_count

        return dp[total_number_of_boxes]
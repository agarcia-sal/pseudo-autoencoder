from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            position_right = fruits[right][0]
            amount_right = fruits[right][1]
            total_fruits += amount_right

            # Shrink window from left if the current window doesn't satisfy conditions
            while left <= right:
                position_left = fruits[left][0]
                # Check fruit positions are within [startPos - k, startPos + k]
                in_range_left = (startPos - k <= position_left <= startPos + k)
                in_range_right = (startPos - k <= position_right <= startPos + k)
                if not (in_range_left and in_range_right):
                    # If either end is not in allowed range, need to move left pointer
                    total_fruits -= fruits[left][1]
                    left += 1
                    continue

                min_dist = min(abs(position_right - startPos), abs(position_left - startPos))
                dist_between = position_right - position_left
                # Check if total travel distance allows collecting all fruits in window
                if min_dist + dist_between <= k:
                    break
                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
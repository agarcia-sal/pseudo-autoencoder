from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            position = fruits[right][0]
            amount = fruits[right][1]
            total_fruits += amount

            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                # Check if both positions are within [startPos - k, startPos + k]
                if not (startPos - k <= left_pos <= startPos + k and startPos - k <= right_pos <= startPos + k):
                    total_fruits -= fruits[left][1]
                    left += 1
                    continue

                dist_left = abs(right_pos - startPos)
                dist_right = abs(left_pos - startPos)
                dist_between = right_pos - left_pos

                # Check movement cost condition
                if min(dist_left, dist_right) + dist_between <= k:
                    break

                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
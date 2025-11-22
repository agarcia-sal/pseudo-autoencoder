from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0
        n = len(fruits)

        for right in range(n):
            pos_right = fruits[right][0]
            amount_right = fruits[right][1]
            total_fruits += amount_right

            while left <= right:
                pos_left = fruits[left][0]
                cond_pos_left = startPos - k <= pos_left <= startPos + k
                cond_pos_right = startPos - k <= pos_right <= startPos + k
                dist_left = abs(pos_left - startPos)
                dist_right = abs(pos_right - startPos)
                # Check if window is valid:
                if cond_pos_left and cond_pos_right and (min(dist_left, dist_right) + (pos_right - pos_left) <= k):
                    break
                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
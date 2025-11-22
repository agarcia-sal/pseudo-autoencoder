from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0
        n = len(fruits)

        for right in range(n):
            pos_right, amount_right = fruits[right]
            total_fruits += amount_right

            while left <= right:
                pos_left = fruits[left][0]
                # Check conditions in the while loop
                cond1 = startPos - k <= pos_left <= startPos + k
                cond2 = startPos - k <= pos_right <= startPos + k
                dist_left = abs(pos_left - startPos)
                dist_right = abs(pos_right - startPos)
                dist_between = pos_right - pos_left
                cond3 = min(dist_left, dist_right) + dist_between <= k
                if cond1 and cond2 and cond3:
                    break
                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
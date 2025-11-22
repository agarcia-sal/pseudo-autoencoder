from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0
        n = len(fruits)

        for right in range(n):
            position_right = fruits[right][0]
            amount_right = fruits[right][1]
            total_fruits += amount_right

            while left <= right:
                position_left = fruits[left][0]
                cond1 = startPos - k <= position_left <= startPos + k
                cond2 = startPos - k <= position_right <= startPos + k
                dist = min(abs(position_right - startPos), abs(position_left - startPos)) + (position_right - position_left)
                if cond1 and cond2 and dist <= k:
                    break
                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
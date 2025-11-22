from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0
        n = len(fruits)

        for right in range(n):
            pos_r, amount_r = fruits[right]
            total_fruits += amount_r

            while left <= right:
                pos_l = fruits[left][0]
                # Check if the segment is within the allowed range and steps
                if not (
                    startPos - k <= pos_l <= startPos + k and
                    startPos - k <= pos_r <= startPos + k and
                    min(abs(pos_r - startPos), abs(pos_l - startPos)) + (pos_r - pos_l) <= k
                ):
                    total_fruits -= fruits[left][1]
                    left += 1
                else:
                    break

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
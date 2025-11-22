from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            pos_right = fruits[right][0]
            amount_right = fruits[right][1]
            total_fruits += amount_right

            while left <= right:
                pos_left = fruits[left][0]
                if not (startPos - k <= pos_left <= startPos + k and
                        startPos - k <= pos_right <= startPos + k and
                        min(abs(pos_right - startPos), abs(pos_left - startPos)) + (pos_right - pos_left) <= k):
                    total_fruits -= fruits[left][1]
                    left += 1
                else:
                    break

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
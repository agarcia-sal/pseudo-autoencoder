from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0
        n = len(fruits)

        for right in range(n):
            position_right, amount_right = fruits[right]
            total_fruits += amount_right

            while left <= right:
                position_left, _ = fruits[left]
                if (startPos - k <= position_left <= startPos + k and
                    startPos - k <= position_right <= startPos + k and
                    min(abs(position_right - startPos), abs(position_left - startPos)) +
                    (position_right - position_left) <= k):
                    break
                total_fruits -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total_fruits)

        return max_fruits
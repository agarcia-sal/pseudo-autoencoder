from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        total_fruits = 0
        left = 0
        n = len(fruits)

        for right in range(n):
            position = fruits[right][0]
            amount = fruits[right][1]
            total_fruits += amount

            while left <= right:
                left_pos = fruits[left][0]
                # Check window validity as per pseudocode conditions
                condition = (
                    startPos - k <= left_pos <= startPos + k
                    and startPos - k <= position <= startPos + k
                    and min(abs(position - startPos), abs(left_pos - startPos)) + abs(position - left_pos) <= k
                )
                if condition:
                    break
                total_fruits -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total_fruits)

        return max_fruits
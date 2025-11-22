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

            # Shrink window while conditions are not met
            while left <= right:
                left_pos = fruits[left][0]

                cond = (
                    startPos - k <= left_pos <= startPos + k and
                    startPos - k <= position <= startPos + k and
                    min(abs(position - startPos), abs(left_pos - startPos)) + (position - left_pos) <= k
                )

                if cond:
                    break

                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
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

            # Shrink window from the left if conditions not satisfied
            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]
                # Check if both ends are within the valid range
                if startPos - k <= left_pos <= startPos + k and startPos - k <= right_pos <= startPos + k:
                    # Calculate minimum steps needed to cover fruits[left] and fruits[right]
                    dist = min(abs(right_pos - startPos), abs(left_pos - startPos)) + (right_pos - left_pos)
                    if dist <= k:
                        break
                total_fruits -= fruits[left][1]
                left += 1

            if max_fruits < total_fruits:
                max_fruits = total_fruits

        return max_fruits
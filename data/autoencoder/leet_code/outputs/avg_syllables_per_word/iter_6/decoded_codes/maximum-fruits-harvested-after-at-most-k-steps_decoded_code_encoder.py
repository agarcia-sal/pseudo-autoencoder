class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            position_right, amount_right = fruits[right]
            total_fruits += amount_right

            while left <= right:
                position_left = fruits[left][0]
                cond = (
                    startPos - k <= position_left <= startPos + k and
                    startPos - k <= position_right <= startPos + k and
                    min(abs(position_right - startPos), abs(position_left - startPos)) + (position_right - position_left) <= k
                )
                if cond:
                    break
                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
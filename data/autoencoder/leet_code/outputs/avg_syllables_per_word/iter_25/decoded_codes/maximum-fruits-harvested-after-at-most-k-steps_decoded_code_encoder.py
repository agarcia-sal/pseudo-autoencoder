class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        max_fruits = 0
        total_fruits = 0
        left = 0
        n = len(fruits)

        for right in range(n):
            position = fruits[right][0]
            amount = fruits[right][1]
            total_fruits += amount

            # Shrink window from left while it doesn't satisfy movement constraints
            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                # Check if left_pos and right_pos are within [startPos - k, startPos + k]
                in_range_left = (startPos - k) <= left_pos <= (startPos + k)
                in_range_right = (startPos - k) <= right_pos <= (startPos + k)

                # Calculate minimal movement cost
                dist_left = abs(left_pos - startPos)
                dist_right = abs(right_pos - startPos)
                interval = right_pos - left_pos
                minimal_move = min(dist_right, dist_left) + interval

                if in_range_left and in_range_right and minimal_move <= k:
                    break

                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
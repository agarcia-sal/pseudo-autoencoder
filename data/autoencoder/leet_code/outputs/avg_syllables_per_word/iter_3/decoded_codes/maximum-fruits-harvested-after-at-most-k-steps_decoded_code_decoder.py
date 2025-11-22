class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            position, amount = fruits[right]
            total_fruits += amount

            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]
                dist = min(abs(right_pos - startPos), abs(left_pos - startPos)) + (right_pos - left_pos)
                if (startPos - k <= left_pos <= startPos + k and
                    startPos - k <= right_pos <= startPos + k and
                    dist <= k):
                    break
                total_fruits -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total_fruits)

        return max_fruits
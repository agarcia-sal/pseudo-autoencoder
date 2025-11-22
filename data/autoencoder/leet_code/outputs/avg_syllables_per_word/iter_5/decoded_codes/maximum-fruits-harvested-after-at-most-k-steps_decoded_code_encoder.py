class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            pos_r, amount_r = fruits[right]
            total_fruits += amount_r

            while left <= right and not (
                startPos - k <= fruits[left][0] <= startPos + k and
                startPos - k <= pos_r <= startPos + k and
                min(abs(pos_r - startPos), abs(fruits[left][0] - startPos)) +
                (pos_r - fruits[left][0]) <= k
            ):
                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
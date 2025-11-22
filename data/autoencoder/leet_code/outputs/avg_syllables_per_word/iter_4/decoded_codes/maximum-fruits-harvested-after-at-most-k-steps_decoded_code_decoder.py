class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            position, amount = fruits[right]
            total_fruits += amount

            while left <= right and not (
                startPos - k <= fruits[left][0] <= startPos + k and
                startPos - k <= fruits[right][0] <= startPos + k and
                min(abs(fruits[right][0] - startPos), abs(fruits[left][0] - startPos)) +
                fruits[right][0] - fruits[left][0] <= k
            ):
                total_fruits -= fruits[left][1]
                left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        max_fruits = 0
        total_fruits = 0
        left = 0

        for right in range(len(fruits)):
            pos_r, amt_r = fruits[right]
            total_fruits += amt_r

            while left <= right:
                pos_l, _ = fruits[left]
                if not (
                    startPos - k <= pos_l <= startPos + k and
                    startPos - k <= pos_r <= startPos + k and
                    min(abs(pos_r - startPos), abs(pos_l - startPos)) + (pos_r - pos_l) <= k
                ):
                    total_fruits -= fruits[left][1]
                    left += 1
                else:
                    break

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
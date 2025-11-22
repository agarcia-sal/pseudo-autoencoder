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
                if not (startPos - k <= left_pos <= startPos + k and startPos - k <= position <= startPos + k):
                    total_fruits -= fruits[left][1]
                    left += 1
                    continue

                dist = min(abs(position - startPos), abs(left_pos - startPos)) + abs(position - left_pos)
                if dist <= k:
                    break
                else:
                    total_fruits -= fruits[left][1]
                    left += 1

            if total_fruits > max_fruits:
                max_fruits = total_fruits

        return max_fruits
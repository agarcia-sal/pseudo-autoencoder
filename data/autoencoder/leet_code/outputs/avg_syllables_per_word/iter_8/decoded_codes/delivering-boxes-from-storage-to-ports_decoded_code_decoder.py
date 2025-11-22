class Solution:
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        n = len(boxes)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        left = 0
        current_weight = 0
        extra_trips = 0

        for right in range(n):
            current_weight += boxes[right][1]
            if right > 0 and boxes[right][0] != boxes[right - 1][0]:
                extra_trips += 1

            while left <= right and (right - left + 1 > maxBoxes or current_weight > maxWeight):
                current_weight -= boxes[left][1]
                if left > 0 and boxes[left][0] != boxes[left - 1][0]:
                    extra_trips -= 1
                left += 1

            dp[right + 1] = dp[left] + 2 + extra_trips

        return dp[n]
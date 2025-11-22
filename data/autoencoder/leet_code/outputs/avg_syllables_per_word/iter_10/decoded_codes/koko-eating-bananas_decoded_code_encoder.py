class Solution:
    def minEatingSpeed(self, piles, h):
        def canFinish(k):
            hours = 0
            for pile in piles:
                hours += -(-pile // k)  # Ceiling division
            return hours <= h

        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
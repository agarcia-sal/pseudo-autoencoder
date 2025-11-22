class Solution:
    def maxRunTime(self, n, batteries):
        def canRunFor(time):
            total = 0
            for battery in batteries:
                total += min(battery, time)
            return total >= time * n

        left = 0
        right = sum(batteries) // n
        while left < right:
            mid = (left + right + 1) // 2
            if canRunFor(mid):
                left = mid
            else:
                right = right - 1
        return left
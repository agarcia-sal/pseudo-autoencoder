class Solution:
    def minTaps(self, n, ranges):
        max_range = [0] * (n + 1)
        for i in range(n + 1):
            if ranges[i] > 0:
                left = max(0, i - ranges[i])
                right = min(n, i + ranges[i])
                max_range[left] = max(max_range[left], right)

        taps = current_end = farthest = 0
        for i in range(n + 1):
            if i > farthest:
                return -1
            if i > current_end:
                taps += 1
                current_end = farthest
            farthest = max(farthest, max_range[i])

        return taps
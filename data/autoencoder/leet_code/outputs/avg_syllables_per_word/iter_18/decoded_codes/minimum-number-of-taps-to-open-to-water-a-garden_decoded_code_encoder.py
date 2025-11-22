class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        max_range = [0] * (n + 1)

        for index in range(n + 1):
            if ranges[index] > 0:
                left = max(0, index - ranges[index])
                right = min(n, index + ranges[index])
                max_range[left] = max(max_range[left], right)

        taps = 0
        current_end = 0
        farthest = 0

        for index in range(n + 1):
            if index > farthest:
                return -1
            if index > current_end:
                taps += 1
                current_end = farthest
            farthest = max(farthest, max_range[index])

        return taps
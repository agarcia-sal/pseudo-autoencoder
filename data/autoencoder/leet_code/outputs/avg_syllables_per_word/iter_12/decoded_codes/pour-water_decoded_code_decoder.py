class Solution:
    def pourWater(self, heights, volume, k):
        n = len(heights)
        for _ in range(volume):
            i = k
            # move left while the next left is lower or equal
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # move right while same height as current
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue

            i = k
            # move right while next right is lower or equal
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # move left while same height as current
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue

            heights[k] += 1

        return heights
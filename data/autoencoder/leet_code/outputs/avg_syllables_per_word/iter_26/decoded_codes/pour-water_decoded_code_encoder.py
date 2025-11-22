from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            i = k
            # move left while next left height is less or equal to current
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # move right while next right height equals current
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue

            i = k
            # move right while next right height is less or equal to current
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # move left while previous left height equals current
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue

            heights[k] += 1

        return heights
from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            i = k
            # Move left while next left height is less or equal to current
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # Move right while current height equals next right height
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue

            i = k
            # Move right while next right height is less or equal to current
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # Move left while current height equals previous left height
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue

            # Otherwise, pour water at index k
            heights[k] += 1

        return heights
from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)

        for _ in range(volume):
            i = k
            # Move left while next left is lower or equal
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # Move right while next right is equal to current
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue

            i = k
            # Move right while next right is lower or equal
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # Move left while previous left is equal to current
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue

            heights[k] += 1

        return heights
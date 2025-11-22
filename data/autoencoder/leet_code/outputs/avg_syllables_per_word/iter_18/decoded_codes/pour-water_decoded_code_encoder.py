from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            i = k
            # Move left while the left height is less or equal to current height
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # Move right while the height on the right is equal to the current height
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue
            i = k
            # Move right while the right height is less or equal to current height
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # Move left while the height on the left is equal to the current height
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue
            heights[k] += 1
        return heights
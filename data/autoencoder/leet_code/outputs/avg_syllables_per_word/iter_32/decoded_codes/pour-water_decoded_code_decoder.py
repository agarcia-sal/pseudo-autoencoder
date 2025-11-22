from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)

        for _ in range(volume):
            i = k
            # Move left while the height to the left is less or equal to the current
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # Move right while heights[i] equals heights[i+1] to find the leftmost lowest spot
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue

            i = k
            # Move right while the height to the right is less or equal to the current
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # Move left while heights[i] equals heights[i-1] to find the rightmost lowest spot
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue

            # If no lower position found on either side, add water at k
            heights[k] += 1

        return heights
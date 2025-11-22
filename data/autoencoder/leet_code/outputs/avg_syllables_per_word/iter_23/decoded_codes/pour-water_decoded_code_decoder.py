from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            i = k
            # Move left while the left height is less or equal than current
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # Move right while heights are equal to find the left-most lowest
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue

            i = k
            # Move right while the right height is less or equal than current
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # Move left while heights are equal to find the right-most lowest
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue

            # If no lower position found, add to kth position
            heights[k] += 1

        return heights
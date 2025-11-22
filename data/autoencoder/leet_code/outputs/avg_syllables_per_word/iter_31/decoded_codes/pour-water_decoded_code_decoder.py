from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            i = k
            # move left if next left is lower or equal height
            while i > 0 and heights[i - 1] <= heights[i]:
                i -= 1
            # move right if heights equal (to find leftmost lowest)
            while i < k and heights[i] == heights[i + 1]:
                i += 1
            if i < k:
                heights[i] += 1
                continue

            i = k
            # move right if next right is lower or equal height
            while i < n - 1 and heights[i + 1] <= heights[i]:
                i += 1
            # move left if heights equal (to find rightmost lowest)
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            if i > k:
                heights[i] += 1
                continue

            # add water at k if cannot move left or right
            heights[k] += 1
        return heights
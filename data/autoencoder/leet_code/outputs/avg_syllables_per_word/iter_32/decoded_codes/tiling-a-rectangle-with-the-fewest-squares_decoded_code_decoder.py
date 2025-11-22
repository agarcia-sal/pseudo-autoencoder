from math import inf
from typing import List

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        min_moves = inf

        def backtrack(heights: List[int], moves: int) -> None:
            nonlocal min_moves

            # If all columns have reached height n, update min_moves
            if all(h == n for h in heights):
                if moves < min_moves:
                    min_moves = moves
                return

            # Prune branches where moves exceed or equal current min_moves
            if moves >= min_moves:
                return

            # Find the leftmost column(s) with minimal height
            min_height = min(heights)
            left = heights.index(min_height)
            right = left

            # Extend right while columns have the same minimal height
            while right < m and heights[right] == min_height:
                right += 1

            max_size = right - left  # max possible square side length here

            # Try placing squares from largest to smallest possible within the segment
            for size in range(max_size, 0, -1):
                if all((heights[left + i] + size) <= n for i in range(size)):
                    new_heights = heights[:]
                    for i in range(size):
                        new_heights[left + i] += size
                    backtrack(new_heights, moves + 1)

        backtrack([0] * m, 0)
        return min_moves
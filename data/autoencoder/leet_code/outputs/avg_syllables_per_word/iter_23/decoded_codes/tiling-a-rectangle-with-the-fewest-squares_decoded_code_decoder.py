import math
from typing import List

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        min_moves = math.inf

        def backtrack(heights: List[int], moves: int) -> None:
            nonlocal min_moves

            if all(height == n for height in heights):
                if moves < min_moves:
                    min_moves = moves
                return

            if moves >= min_moves:
                return

            min_height = min(heights)
            left = heights.index(min_height)
            right = left
            while right < m and heights[right] == min_height:
                right += 1

            max_square_size = right - left
            for size in range(max_square_size, 0, -1):
                # check if placing square of size fits vertically within the rectangle
                if all(heights[left + i] + size <= n for i in range(size)):
                    new_heights = heights[:]
                    for i in range(size):
                        new_heights[left + i] += size
                    backtrack(new_heights, moves + 1)

        backtrack([0] * m, 0)
        return min_moves
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        min_moves = float('inf')

        def backtrack(heights, moves):
            nonlocal min_moves
            min_height = min(heights)
            if all(h == n for h in heights):
                if moves < min_moves:
                    min_moves = moves
                return
            if moves >= min_moves:
                return
            left = heights.index(min_height)
            right = left
            while right < m and heights[right] == min_height:
                right += 1
            max_size = right - left
            for size in range(max_size, 0, -1):
                if all(heights[left + i] + size <= n for i in range(size)):
                    new_heights = heights[:]
                    for i in range(size):
                        new_heights[left + i] += size
                    backtrack(new_heights, moves + 1)

        backtrack([0] * m, 0)
        return min_moves
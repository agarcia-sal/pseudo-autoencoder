class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        min_moves = float('inf')

        def backtrack(heights, current_moves):
            nonlocal min_moves
            if all(h == n for h in heights):
                min_moves = min(min_moves, current_moves)
                return
            if current_moves >= min_moves:
                return

            min_height = min(heights)
            left = heights.index(min_height)
            right = left
            while right < m and heights[right] == min_height:
                right += 1

            max_size = right - left
            for size in range(max_size, 0, -1):
                # Check if we can place a square of 'size' here without exceeding n
                if all(heights[left + i] + size <= n for i in range(size)):
                    new_heights = heights[:]
                    for i in range(size):
                        new_heights[left + i] += size
                    backtrack(new_heights, current_moves + 1)

        backtrack([0] * m, 0)
        return min_moves
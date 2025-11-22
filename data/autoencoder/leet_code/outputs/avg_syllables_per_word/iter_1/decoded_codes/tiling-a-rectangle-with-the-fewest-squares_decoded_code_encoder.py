def tilingRectangle(n, m):
    min_moves = float('inf')

    def backtrack(heights, moves):
        nonlocal min_moves
        if all(h == n for h in heights):
            min_moves = min(min_moves, moves)
            return
        if moves >= min_moves:
            return

        min_h = min(heights)
        left = heights.index(min_h)
        right = left
        while right < m and heights[right] == min_h:
            right += 1

        max_size = right - left
        for size in range(max_size, 0, -1):
            if all(heights[left + i] + size <= n for i in range(size)):
                new_h = heights[:]
                for i in range(size):
                    new_h[left + i] += size
                backtrack(new_h, moves + 1)

    backtrack([0] * m, 0)
    return min_moves
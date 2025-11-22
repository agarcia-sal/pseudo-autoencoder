from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add the restriction for building 1 with height 0
        restrictions.append([1, 0])
        # Sort by position, then by height
        restrictions.sort(key=lambda x: (x[0], x[1]))

        # Forward pass: ensure restrictions respect height differences from left to right
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            prev_idx, prev_height = restrictions[i - 1]
            # Height at current cannot exceed prev_height + distance difference
            restrictions[i][1] = min(height, prev_height + idx - prev_idx)

        # Backward pass: ensure restrictions respect height differences from right to left
        for i in range(len(restrictions) - 2, -1, -1):
            idx, height = restrictions[i]
            next_idx, next_height = restrictions[i + 1]
            restrictions[i][1] = min(height, next_height + next_idx - idx)

        max_height = 0
        prev_idx, prev_height = restrictions[0]

        # Check max height between every two adjacent restrictions
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            distance = idx - prev_idx
            # The tallest possible building between two restrictions forms a 'peak'
            candidate_height = (distance + prev_height + height) // 2
            if candidate_height > max_height:
                max_height = candidate_height
            prev_idx, prev_height = idx, height

        # Possible tallest building after last restriction up to building n
        candidate_height = prev_height + n - prev_idx
        if candidate_height > max_height:
            max_height = candidate_height

        return max_height
from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add restriction for building 1 with height 0
        restrictions.append([1, 0])
        # Sort restrictions by building index
        restrictions.sort(key=lambda x: x[0])

        # Forward pass to adjust heights to satisfy slope constraints
        for i in range(1, len(restrictions)):
            curr_idx, curr_h = restrictions[i]
            prev_idx, prev_h = restrictions[i - 1]
            allowed_height = prev_h + (curr_idx - prev_idx)
            restrictions[i][1] = min(curr_h, allowed_height)

        # Backward pass to adjust heights similarly
        for i in range(len(restrictions) - 2, -1, -1):
            curr_idx, curr_h = restrictions[i]
            next_idx, next_h = restrictions[i + 1]
            allowed_height = next_h + (next_idx - curr_idx)
            restrictions[i][1] = min(curr_h, allowed_height)

        max_height = 0
        prev_idx, prev_h = restrictions[0]

        # Calculate max possible height between restrictions
        for i in range(1, len(restrictions)):
            curr_idx, curr_h = restrictions[i]
            dist = curr_idx - prev_idx
            height_diff = abs(curr_h - prev_h)
            # Max height achievable on path between prev and curr restrictions
            # is midway plus the integer division
            peak_height = (prev_h + curr_h + dist) // 2
            max_height = max(max_height, peak_height)
            prev_idx, prev_h = curr_idx, curr_h

        # Check max height from last restriction to building n
        max_height = max(max_height, prev_h + (n - prev_idx))

        return max_height
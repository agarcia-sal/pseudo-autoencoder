from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add the starting building with height 0 at index 1
        restrictions.append([1, 0])
        # Sort by building index
        restrictions.sort(key=lambda x: x[0])

        # Forward pass: ensure each restriction respects increase constraint from previous
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            prev_idx, prev_height = restrictions[i-1]
            restrictions[i][1] = min(height, prev_height + (idx - prev_idx))

        # Backward pass: ensure each restriction respects increase constraint from next
        for i in range(len(restrictions) - 2, -1, -1):
            idx, height = restrictions[i]
            next_idx, next_height = restrictions[i+1]
            restrictions[i][1] = min(height, next_height + (next_idx - idx))

        max_height = 0
        prev_idx, prev_height = restrictions[0]

        # For each interval between consecutive restricted buildings,
        # find the maximum possible height considering the linear slope constraints
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            # The maximum height is achieved at the midpoint between prev_idx and idx,
            # capped by the heights at both ends and the distance between the buildings.
            candidate = ( (idx - prev_idx) + prev_height + height ) // 2
            if candidate > max_height:
                max_height = candidate
            prev_idx, prev_height = idx, height

        # Check possibility of increasing height after the last restriction until building n
        candidate = prev_height + (n - prev_idx)
        if candidate > max_height:
            max_height = candidate

        return max_height
from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        # Forward pass to adjust heights based on previous restriction
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            prev_idx, prev_height = restrictions[i - 1]
            restrictions[i][1] = min(height, prev_height + idx - prev_idx)

        # Backward pass to adjust heights based on next restriction
        for i in range(len(restrictions) - 2, -1, -1):
            idx, height = restrictions[i]
            next_idx, next_height = restrictions[i + 1]
            restrictions[i][1] = min(height, next_height + next_idx - idx)

        max_height = 0
        prev_idx, prev_height = restrictions[0]

        # Calculate max height achievable between restrictions
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            local_max = (idx - prev_idx + prev_height + height) // 2
            if local_max > max_height:
                max_height = local_max
            prev_idx, prev_height = idx, height

        max_height = max(max_height, prev_height + (n - prev_idx))
        return max_height
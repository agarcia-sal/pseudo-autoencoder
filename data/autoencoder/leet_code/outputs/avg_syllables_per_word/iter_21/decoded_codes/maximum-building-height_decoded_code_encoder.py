from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort(key=lambda x: x[0])

        # Forward pass: update heights based on previous restrictions
        for i in range(1, len(restrictions)):
            curr_idx, curr_h = restrictions[i]
            prev_idx, prev_h = restrictions[i-1]
            restrictions[i][1] = min(curr_h, prev_h + (curr_idx - prev_idx))

        # Backward pass: update heights based on next restrictions
        for i in range(len(restrictions) - 2, -1, -1):
            curr_idx, curr_h = restrictions[i]
            next_idx, next_h = restrictions[i+1]
            restrictions[i][1] = min(curr_h, next_h + (next_idx - curr_idx))

        max_height = 0
        prev_idx, prev_h = restrictions[0]

        # Calculate maximum achievable height between restrictions
        for i in range(1, len(restrictions)):
            curr_idx, curr_h = restrictions[i]
            candidate = (curr_idx - prev_idx + prev_h + curr_h) // 2
            max_height = max(max_height, candidate)
            prev_idx, prev_h = curr_idx, curr_h

        max_height = max(max_height, prev_h + (n - prev_idx))

        return max_height
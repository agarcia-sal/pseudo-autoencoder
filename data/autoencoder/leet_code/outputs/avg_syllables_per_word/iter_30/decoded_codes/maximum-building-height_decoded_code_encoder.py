from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add restriction for building 1 with height 0
        restrictions.append([1, 0])
        restrictions.sort(key=lambda x: x[0])

        # Forward pass: ensure heights are consistent with increasing indices
        for i in range(1, len(restrictions)):
            cur_i, cur_h = restrictions[i]
            prev_i, prev_h = restrictions[i - 1]
            max_h = prev_h + (cur_i - prev_i)
            restrictions[i][1] = min(cur_h, max_h)

        # Backward pass: ensure heights are consistent with decreasing indices
        for i in range(len(restrictions) - 2, -1, -1):
            cur_i, cur_h = restrictions[i]
            next_i, next_h = restrictions[i + 1]
            max_h = next_h + (next_i - cur_i)
            restrictions[i][1] = min(cur_h, max_h)

        max_height = 0
        prev_i, prev_h = restrictions[0]

        # Calculate maximum possible building height between restrictions
        for i in range(1, len(restrictions)):
            cur_i, cur_h = restrictions[i]
            # Candidate max height is the peak of the "tent"
            candidate_height = (cur_i - prev_i + prev_h + cur_h) // 2
            if candidate_height > max_height:
                max_height = candidate_height
            prev_i, prev_h = cur_i, cur_h

        # Consider the stretch from the last restriction to building n
        max_height = max(max_height, restrictions[-1][1] + n - restrictions[-1][0])

        return max_height
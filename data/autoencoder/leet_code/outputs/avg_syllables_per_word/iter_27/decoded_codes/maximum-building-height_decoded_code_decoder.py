from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Append (1, 0) restriction as per problem statement
        restrictions.append([1, 0])
        restrictions.sort(key=lambda x: x[0])

        # Forward pass to enforce height limits based on previous restrictions
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            prev_idx, prev_height = restrictions[i - 1]
            # height cannot exceed prev_height + distance (idx - prev_idx)
            restrictions[i][1] = min(height, prev_height + (idx - prev_idx))

        # Backward pass to enforce height limits based on next restrictions
        for i in range(len(restrictions) - 2, -1, -1):
            idx, height = restrictions[i]
            next_idx, next_height = restrictions[i + 1]
            # height cannot exceed next_height + distance (next_idx - idx)
            restrictions[i][1] = min(height, next_height + (next_idx - idx))

        max_height = 0
        prev_idx, prev_height = restrictions[0]

        # Iterate through restrictions to find max possible building height between restrictions
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            # The highest possible building between prev and current restriction is when the slope intersects
            candidate_height = (idx - prev_idx + prev_height + height) // 2
            if candidate_height > max_height:
                max_height = candidate_height
            prev_idx, prev_height = idx, height

        # Consider extending after last restriction to building n
        max_height = max(max_height, prev_height + n - prev_idx)

        return max_height
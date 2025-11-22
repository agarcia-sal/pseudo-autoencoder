from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add the restriction for building 1 with height 0
        restrictions.append([1, 0])
        # Sort restrictions by building index
        restrictions.sort(key=lambda x: x[0])

        # Forward pass to adjust heights considering previous restriction
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            prev_idx, prev_height = restrictions[i - 1]
            allowed_height = prev_height + (idx - prev_idx)
            if height > allowed_height:
                restrictions[i][1] = allowed_height

        # Backward pass to adjust heights considering next restriction
        for i in range(len(restrictions) - 2, -1, -1):
            idx, height = restrictions[i]
            next_idx, next_height = restrictions[i + 1]
            allowed_height = next_height + (next_idx - idx)
            if height > allowed_height:
                restrictions[i][1] = allowed_height

        max_height = 0
        prev_idx, prev_height = restrictions[0]

        # Traverse restrictions to find max possible height in gaps
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            # The tallest building in the gap is limited by the line between prev and current restrictions
            candidate_height = ( (idx - prev_idx) + prev_height + height ) // 2
            if candidate_height > max_height:
                max_height = candidate_height
            prev_idx, prev_height = idx, height

        # Consider potential height after last restriction to building n
        poss_height_after_last = prev_height + (n - prev_idx)
        if poss_height_after_last > max_height:
            max_height = poss_height_after_last

        return max_height
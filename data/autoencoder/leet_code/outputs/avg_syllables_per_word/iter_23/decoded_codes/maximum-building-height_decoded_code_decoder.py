from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort(key=lambda x: x[0])

        for i in range(1, len(restrictions)):
            current_pos = restrictions[i][0]
            current_height = restrictions[i][1]
            prev_pos = restrictions[i-1][0]
            prev_height = restrictions[i-1][1]
            restrictions[i][1] = min(current_height, prev_height + current_pos - prev_pos)

        for i in range(len(restrictions) - 2, -1, -1):
            current_pos = restrictions[i][0]
            current_height = restrictions[i][1]
            next_pos = restrictions[i+1][0]
            next_height = restrictions[i+1][1]
            restrictions[i][1] = min(current_height, next_height + next_pos - current_pos)

        max_height = 0
        prev_pos = restrictions[0][0]
        prev_height = restrictions[0][1]

        for i in range(1, len(restrictions)):
            current_pos = restrictions[i][0]
            current_height = restrictions[i][1]
            candidate_height = (current_pos - prev_pos + prev_height + current_height) // 2
            if candidate_height > max_height:
                max_height = candidate_height
            prev_pos = current_pos
            prev_height = current_height

        final_candidate_height = prev_height + (n - prev_pos)
        if final_candidate_height > max_height:
            max_height = final_candidate_height

        return max_height
from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort(key=lambda x: x[0])

        for i in range(1, len(restrictions)):
            curr_pos, curr_height = restrictions[i]
            prev_pos, prev_height = restrictions[i - 1]
            restrictions[i][1] = min(curr_height, prev_height + curr_pos - prev_pos)

        for i in range(len(restrictions) - 2, -1, -1):
            curr_pos, curr_height = restrictions[i]
            next_pos, next_height = restrictions[i + 1]
            restrictions[i][1] = min(curr_height, next_height + next_pos - curr_pos)

        max_height = 0
        prev_pos, prev_height = restrictions[0]

        for i in range(1, len(restrictions)):
            curr_pos, curr_height = restrictions[i]
            candidate_height = (curr_pos - prev_pos + prev_height + curr_height) // 2
            if candidate_height > max_height:
                max_height = candidate_height
            prev_pos, prev_height = curr_pos, curr_height

        max_height = max(max_height, prev_height + n - prev_pos)

        return max_height
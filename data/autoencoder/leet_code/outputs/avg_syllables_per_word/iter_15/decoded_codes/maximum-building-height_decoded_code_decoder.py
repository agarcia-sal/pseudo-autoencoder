from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        for i in range(1, len(restrictions)):
            cur_idx, cur_h = restrictions[i]
            prev_idx, prev_h = restrictions[i - 1]
            restrictions[i][1] = min(cur_h, prev_h + cur_idx - prev_idx)

        for i in range(len(restrictions) - 2, -1, -1):
            cur_idx, cur_h = restrictions[i]
            next_idx, next_h = restrictions[i + 1]
            restrictions[i][1] = min(cur_h, next_h + next_idx - cur_idx)

        max_height = 0
        prev_idx, prev_h = restrictions[0]

        for i in range(1, len(restrictions)):
            cur_idx, cur_h = restrictions[i]
            possible_height = (cur_idx - prev_idx + prev_h + cur_h) // 2
            max_height = max(max_height, possible_height)
            prev_idx, prev_h = cur_idx, cur_h

        max_height = max(max_height, prev_h + n - prev_idx)

        return max_height
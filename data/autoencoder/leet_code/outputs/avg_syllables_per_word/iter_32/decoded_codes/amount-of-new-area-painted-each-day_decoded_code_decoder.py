from typing import List

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        max_end = max(end for _, end in paint) if paint else 0
        painted = [-1] * (max_end + 1)
        worklog = []

        for start, end in paint:
            current_start = start
            new_paint = 0

            while current_start < end:
                if painted[current_start] == -1:
                    painted[current_start] = end
                    new_paint += 1
                    current_start += 1
                else:
                    current_start = painted[current_start]

            worklog.append(new_paint)

        return worklog
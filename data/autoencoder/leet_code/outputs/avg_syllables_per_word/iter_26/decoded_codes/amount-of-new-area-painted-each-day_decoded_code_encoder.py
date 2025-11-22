from typing import List

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        max_end = max(end for _, end in paint)
        painted = [-1] * (max_end + 1)
        result = []

        for start, end in paint:
            current = start
            painted_amount = 0

            while current < end:
                if painted[current] == -1:
                    painted[current] = end
                    painted_amount += 1
                    current += 1
                else:
                    current = painted[current]

            result.append(painted_amount)

        return result
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        prev_red = costs[0][0]
        prev_blue = costs[0][1]
        prev_green = costs[0][2]

        for i in range(1, len(costs)):
            current_red = costs[i][0] + min(prev_blue, prev_green)
            current_blue = costs[i][1] + min(prev_red, prev_green)
            current_green = costs[i][2] + min(prev_red, prev_blue)

            prev_red, prev_blue, prev_green = current_red, current_blue, current_green

        return min(prev_red, prev_blue, prev_green)
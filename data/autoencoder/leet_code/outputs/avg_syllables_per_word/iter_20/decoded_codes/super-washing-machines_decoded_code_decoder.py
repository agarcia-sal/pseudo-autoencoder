from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        if total_dresses % n != 0:
            return -1

        target = total_dresses // n
        left_sum = 0
        max_moves = 0

        for i in range(n):
            left_excess = left_sum - target * i
            right_excess = (total_dresses - left_sum - machines[i]) - target * (n - i - 1)
            current_moves = max(abs(left_excess), abs(right_excess), machines[i] - target)
            max_moves = max(max_moves, current_moves)
            left_sum += machines[i]

        return max_moves
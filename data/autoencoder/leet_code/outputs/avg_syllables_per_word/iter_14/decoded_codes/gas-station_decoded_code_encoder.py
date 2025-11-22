from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total_tank = 0

        for index in range(len(gas)):
            total_tank += gas[index] - cost[index]
            if total_tank < 0:
                start = index + 1
                total_tank = 0

        return start
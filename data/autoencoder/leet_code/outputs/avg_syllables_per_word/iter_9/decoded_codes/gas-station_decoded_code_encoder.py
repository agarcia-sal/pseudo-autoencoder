class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total_tank = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            if total_tank < 0:
                start = i + 1
                total_tank = 0

        return start
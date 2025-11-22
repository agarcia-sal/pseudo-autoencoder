class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        n = len(distance)
        if n < 4:
            return False

        for i in range(3, n):
            # Case 1: current line crosses the line 3 steps behind
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True

            # Case 2: current line meets the line 4 steps behind
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True

            # Case 3: current line crosses the line 5 steps behind
            if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i - 3] >= distance[i - 1] \
                    and distance[i - 1] + distance[i - 5] >= distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True

        return False
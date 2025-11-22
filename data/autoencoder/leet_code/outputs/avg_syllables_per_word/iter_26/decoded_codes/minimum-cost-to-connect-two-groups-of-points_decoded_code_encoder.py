from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size_one = len(cost)
        size_two = len(cost[0])

        dp_table = [[inf] * (1 << size_two) for _ in range(size_one + 1)]
        dp_table[0][0] = 0

        for i in range(size_one):
            for mask in range(1 << size_two):
                # Try to connect group i to a new element j in group two
                for j in range(size_two):
                    next_mask = mask | (1 << j)
                    dp_table[i + 1][next_mask] = min(
                        dp_table[i + 1][next_mask],
                        dp_table[i][mask] + cost[i][j]
                    )
                # Also consider leaving current mask unchanged
                for j in range(size_two):
                    if mask & (1 << j):
                        dp_table[i + 1][mask] = min(
                            dp_table[i + 1][mask],
                            dp_table[i + 1][mask ^ (1 << j)] + cost[i][j]
                        )
        return dp_table[size_one][(1 << size_two) - 1]
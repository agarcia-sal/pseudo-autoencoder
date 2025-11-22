from math import comb

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        def count_ways(arr):
            if len(arr) <= 1:
                return 1

            root = arr[0]
            left_subtree = []
            right_subtree = []

            for x in arr[1:]:
                if x < root:
                    left_subtree.append(x)
                elif x > root:
                    right_subtree.append(x)

            ways_left = count_ways(left_subtree)
            ways_right = count_ways(right_subtree)

            total_ways = comb(len(left_subtree) + len(right_subtree), len(left_subtree))
            return (ways_left * ways_right * total_ways) % MOD

        return (count_ways(nums) - 1) % MOD
from math import comb
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def count_ways(arr: List[int]) -> int:
            if len(arr) <= 1:
                return 1

            root = arr[0]
            left_subtree = [x for x in arr if x < root]
            right_subtree = [x for x in arr if x > root]

            ways_left = count_ways(left_subtree)
            ways_right = count_ways(right_subtree)
            total_ways = comb(len(left_subtree) + len(right_subtree), len(left_subtree)) % MOD

            return (ways_left * ways_right * total_ways) % MOD

        return (count_ways(nums) - 1) % MOD
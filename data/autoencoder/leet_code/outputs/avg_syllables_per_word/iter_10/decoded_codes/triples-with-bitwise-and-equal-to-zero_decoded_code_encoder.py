from collections import defaultdict

class Solution:
    def countTriplets(self, nums):
        pair_and_count = defaultdict(int)
        for i in nums:
            for j in nums:
                pair_and_count[i & j] += 1

        triplet_count = 0
        for k in nums:
            for pair_and, count in pair_and_count.items():
                if (pair_and & k) == 0:
                    triplet_count += count
        return triplet_count
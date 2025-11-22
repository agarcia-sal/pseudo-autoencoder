from collections import defaultdict

class Solution:
    def countTriplets(self, nums):
        pair_and_count = defaultdict(int)
        for first_number in nums:
            for second_number in nums:
                bitwise_and_result = first_number & second_number
                pair_and_count[bitwise_and_result] += 1

        triplet_count = 0
        for k_number in nums:
            for pair_and, count in pair_and_count.items():
                if (pair_and & k_number) == 0:
                    triplet_count += count
        return triplet_count
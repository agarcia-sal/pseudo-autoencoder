from collections import defaultdict
from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        pair_and_count = defaultdict(int)
        for first_number in nums:
            for second_number in nums:
                bitwise_and_result = first_number & second_number
                pair_and_count[bitwise_and_result] += 1

        triplet_count = 0
        for candidate_number in nums:
            for bitwise_and_key, frequency_value in pair_and_count.items():
                if (bitwise_and_key & candidate_number) == 0:
                    triplet_count += frequency_value

        return triplet_count
from collections import defaultdict
from typing import List

class Solution:
    def countTriplets(self, list_of_numbers: List[int]) -> int:
        pair_freq = defaultdict(int)

        for first_number in list_of_numbers:
            for second_number in list_of_numbers:
                pair_freq[first_number & second_number] += 1

        triplet_total_count = 0

        for candidate_number in list_of_numbers:
            for pair_and_value, count in pair_freq.items():
                if (pair_and_value & candidate_number) == 0:
                    triplet_total_count += count

        return triplet_total_count
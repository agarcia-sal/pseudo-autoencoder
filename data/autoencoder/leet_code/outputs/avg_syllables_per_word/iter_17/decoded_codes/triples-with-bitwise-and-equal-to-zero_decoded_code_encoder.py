from collections import defaultdict

class Solution:
    def countTriplets(self, list_of_numbers):
        pair_and_count_mapping = defaultdict(int)

        for first_number in list_of_numbers:
            for second_number in list_of_numbers:
                bitwise_and_result = first_number & second_number
                pair_and_count_mapping[bitwise_and_result] += 1

        total_triplet_count = 0
        for current_number in list_of_numbers:
            for bitwise_and_key, associated_count in pair_and_count_mapping.items():
                if (bitwise_and_key & current_number) == 0:
                    total_triplet_count += associated_count

        return total_triplet_count
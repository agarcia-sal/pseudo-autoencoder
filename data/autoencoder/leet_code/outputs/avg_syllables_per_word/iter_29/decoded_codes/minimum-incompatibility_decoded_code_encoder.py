from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums, k):
        integer_n = len(nums)
        integer_subset_size = integer_n // k

        def all_numbers_appear_no_more_than_k_times(list_of_numbers, max_count):
            count = Counter(list_of_numbers)
            for c in count.values():
                if c > max_count:
                    return False
            return True

        if not all_numbers_appear_no_more_than_k_times(nums, k):
            return -1

        subset_incompatibility = {}

        def count_number_of_set_bits_in_integer(integer_value):
            bit_count = 0
            working_value = integer_value
            while working_value > 0:
                bit_count += working_value & 1
                working_value >>= 1
            return bit_count

        total_mask_limit = 1 << integer_n

        def all_elements_unique(list_of_elements):
            return len(set(list_of_elements)) == len(list_of_elements)

        for mask in range(total_mask_limit):
            if count_number_of_set_bits_in_integer(mask) == integer_subset_size:
                current_elements = [
                    nums[index]
                    for index in range(integer_n)
                    if (mask & (1 << index)) != 0
                ]
                if all_elements_unique(current_elements):
                    incompatibility_value = max(current_elements) - min(current_elements)
                    subset_incompatibility[mask] = incompatibility_value

        dp = [float('inf')] * total_mask_limit
        dp[0] = 0

        def minimum_of_two_numbers(first_number, second_number):
            return first_number if first_number < second_number else second_number

        def is_subset(subset, main_set):
            return (subset & main_set) == subset

        for mask in range(total_mask_limit):
            if (count_number_of_set_bits_in_integer(mask) % integer_subset_size) != 0:
                continue
            for subset_mask in subset_incompatibility:
                if is_subset(subset_mask, mask):
                    candidate_value = dp[mask ^ subset_mask] + subset_incompatibility[subset_mask]
                    dp[mask] = minimum_of_two_numbers(dp[mask], candidate_value)

        final_mask = total_mask_limit - 1
        if dp[final_mask] != float('inf'):
            return dp[final_mask]
        else:
            return -1
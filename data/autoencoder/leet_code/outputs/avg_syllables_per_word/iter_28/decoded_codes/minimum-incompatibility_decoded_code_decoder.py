from typing import List
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k

        def has_any_number_appearing_more_than_k_times(numbers: List[int], times: int) -> bool:
            counts = {}
            for number in numbers:
                counts[number] = counts.get(number, 0) + 1
            return any(count > times for count in counts.values())

        if has_any_number_appearing_more_than_k_times(nums, k):
            return -1

        subset_incompatibility = {}

        def count_set_bits_of_integer(number: int) -> int:
            count = 0
            while number > 0:
                count += number & 1
                number >>= 1
            return count

        def elements_in_mask(mask_array: List[int], full_list: List[int]) -> List[int]:
            extracted_elements = []
            for index in range(n):
                if mask_array[index] == 1:
                    extracted_elements.append(full_list[index])
            return extracted_elements

        def mask_to_array(mask: int, length: int) -> List[int]:
            bits_array = []
            for position in range(length):
                bit_value = (mask >> position) & 1
                bits_array.append(bit_value)
            return bits_array

        for mask in range(1 << n):
            bit_count = count_set_bits_of_integer(mask)
            if bit_count == subset_size:
                mask_array = mask_to_array(mask, n)
                elements = elements_in_mask(mask_array, nums)
                element_uniqueness_checker = {}
                for element in elements:
                    element_uniqueness_checker[element] = element_uniqueness_checker.get(element, 0) + 1
                if all(count == 1 for count in element_uniqueness_checker.values()):
                    maximum_element = max(elements)
                    minimum_element = min(elements)
                    incompatibility_value = maximum_element - minimum_element
                    subset_incompatibility[mask] = incompatibility_value

        dp = [inf] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            bit_count = count_set_bits_of_integer(mask)
            if bit_count % subset_size != 0:
                continue
            for subset_mask, incompatibility_value in subset_incompatibility.items():
                if (mask & subset_mask) == subset_mask:
                    current_value = dp[mask]
                    candidate_value = dp[mask ^ subset_mask] + incompatibility_value
                    if candidate_value < current_value:
                        dp[mask] = candidate_value

        final_mask = (1 << n) - 1
        return dp[final_mask] if dp[final_mask] != inf else -1
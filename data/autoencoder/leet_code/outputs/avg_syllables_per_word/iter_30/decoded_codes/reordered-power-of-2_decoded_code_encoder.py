class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        collection_of_sorted_digits_of_powers_of_two = set()
        current_power_of_two = 1
        while current_power_of_two <= 10**9:
            collection_of_sorted_digits_of_powers_of_two.add(tuple(sorted(str(current_power_of_two))))
            current_power_of_two <<= 1  # Multiply by 2 efficiently
        sorted_n_digits = tuple(sorted(str(n)))
        return sorted_n_digits in collection_of_sorted_digits_of_powers_of_two
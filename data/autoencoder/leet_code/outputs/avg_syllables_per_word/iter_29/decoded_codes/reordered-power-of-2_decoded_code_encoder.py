class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        collection_of_sorted_digit_tuples_of_powers_of_two = set()
        current_power_of_two = 1
        while current_power_of_two <= 10**9:
            tuple_of_chars = tuple(sorted(str(current_power_of_two)))
            collection_of_sorted_digit_tuples_of_powers_of_two.add(tuple_of_chars)
            current_power_of_two <<= 1
        tuple_of_chars_n = tuple(sorted(str(n)))
        return tuple_of_chars_n in collection_of_sorted_digit_tuples_of_powers_of_two
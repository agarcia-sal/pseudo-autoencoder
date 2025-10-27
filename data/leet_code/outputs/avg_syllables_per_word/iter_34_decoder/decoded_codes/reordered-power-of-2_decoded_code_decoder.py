class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_two_sorted_digits = set()
        power_of_two = 1
        limit = 10 ** 9
        while power_of_two <= limit:
            sorted_digits = tuple(sorted(str(power_of_two)))
            power_of_two_sorted_digits.add(sorted_digits)
            power_of_two <<= 1  # Multiply by two efficiently
        sorted_n_digits = tuple(sorted(str(n)))
        return sorted_n_digits in power_of_two_sorted_digits
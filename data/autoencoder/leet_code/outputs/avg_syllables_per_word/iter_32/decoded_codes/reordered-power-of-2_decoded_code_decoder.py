class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2_sorted_digits = set()
        power_of_2 = 1
        max_limit = 10**9
        while power_of_2 <= max_limit:
            sorted_digits = tuple(sorted(str(power_of_2)))
            power_of_2_sorted_digits.add(sorted_digits)
            power_of_2 <<= 1  # multiply by 2 efficiently

        sorted_n_digits = tuple(sorted(str(n)))
        return sorted_n_digits in power_of_2_sorted_digits
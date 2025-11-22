class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2_sorted_digits = set()
        power_of_2 = 1
        while power_of_2 <= 10**9:
            current_power_string = str(power_of_2)
            sorted_digits = tuple(sorted(current_power_string))
            power_of_2_sorted_digits.add(sorted_digits)
            power_of_2 *= 2

        n_string = str(n)
        sorted_n_digits = tuple(sorted(n_string))
        return sorted_n_digits in power_of_2_sorted_digits
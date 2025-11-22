class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2_sorted_digits = set()
        power_of_2 = 1
        while power_of_2 <= 1000000000:
            power_of_2_sorted_digits.add(tuple(sorted(str(power_of_2))))
            power_of_2 <<= 1  # multiply by 2 using bit shift
        sorted_n_digits = tuple(sorted(str(n)))
        return sorted_n_digits in power_of_2_sorted_digits
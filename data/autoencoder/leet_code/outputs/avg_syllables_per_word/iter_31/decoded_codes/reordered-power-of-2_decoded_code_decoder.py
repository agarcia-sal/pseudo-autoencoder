class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2_sorted_digits = set()
        power_of_2 = 1
        limit = 10**9  # 1,000,000,000 as the upper bound as per pseudocode (10^9)

        while power_of_2 <= limit:
            digits_tuple = tuple(sorted(str(power_of_2)))
            power_of_2_sorted_digits.add(digits_tuple)
            power_of_2 <<= 1  # multiply by 2 efficiently

        sorted_n_digits = tuple(sorted(str(n)))
        return sorted_n_digits in power_of_2_sorted_digits
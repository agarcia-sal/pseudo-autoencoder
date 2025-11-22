class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2_sorted_digits = set()
        power_of_2 = 1
        limit = 10 ** 9
        while power_of_2 <= limit:
            power_of_2_sorted_digits.add(tuple(sorted(str(power_of_2))))
            power_of_2 <<= 1
        return tuple(sorted(str(n))) in power_of_2_sorted_digits
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2_sorted_digits = self.initializePowerSetUpToOneBillion()
        sorted_n_digits = self.convertNumberToSortedDigitTuple(n)
        return sorted_n_digits in power_of_2_sorted_digits

    def initializePowerSetUpToOneBillion(self):
        power_of_2_sorted_digits = set()
        power_of_2 = 1
        limit = 10**9
        while power_of_2 <= limit:
            digits_of_power = self.convertNumberToSortedDigitTuple(power_of_2)
            power_of_2_sorted_digits.add(digits_of_power)
            power_of_2 <<= 1  # multiply by 2 efficiently
        return power_of_2_sorted_digits

    def convertNumberToSortedDigitTuple(self, number: int):
        return tuple(sorted(str(number)))
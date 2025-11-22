from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Insert '+' before each '-' to split easily, except possibly at start
        string_to_process = expression.replace('-', '+-')
        list_of_fraction_strings = string_to_process.split('+')
        list_of_non_empty_fraction_strings = [fs for fs in list_of_fraction_strings if fs]
        list_of_fractions = [Fraction(frac_str) for frac_str in list_of_non_empty_fraction_strings]
        result_fraction = sum(list_of_fractions, Fraction(0, 1))
        numerator_value = result_fraction.numerator
        denominator_value = result_fraction.denominator
        result_string = f"{numerator_value}/{denominator_value}"
        return result_string
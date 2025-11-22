from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Replace '-' with '+-' to split on '+', then filter out empty strings
        list_of_fractions = expression.replace('-', '+-').split('+')
        result_fraction = Fraction(0, 1)
        for fraction_string in list_of_fractions:
            if fraction_string:
                result_fraction += Fraction(fraction_string)
        return f"{result_fraction.numerator}/{result_fraction.denominator}"
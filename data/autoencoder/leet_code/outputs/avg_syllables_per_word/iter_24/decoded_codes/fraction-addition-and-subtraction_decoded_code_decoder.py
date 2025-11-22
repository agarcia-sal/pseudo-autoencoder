from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        list_of_fractions = expression.replace('-', '+-').split('+')
        sum_of_fractions = Fraction(0, 1)
        for fraction_string in list_of_fractions:
            if fraction_string:
                sum_of_fractions += Fraction(fraction_string)
        return f"{sum_of_fractions.numerator}/{sum_of_fractions.denominator}"
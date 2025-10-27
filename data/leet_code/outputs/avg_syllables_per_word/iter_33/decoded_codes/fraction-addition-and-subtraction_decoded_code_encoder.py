from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Replace '-' with '+-' to split all fractions correctly by '+'
        list_of_fractions = expression.replace('-', '+-').split('+')
        # Filter out empty strings resulted from split
        fractions = [Fraction(frac) for frac in list_of_fractions if frac]
        sum_of_fractions = sum(fractions, Fraction(0))
        return f"{sum_of_fractions.numerator}/{sum_of_fractions.denominator}"
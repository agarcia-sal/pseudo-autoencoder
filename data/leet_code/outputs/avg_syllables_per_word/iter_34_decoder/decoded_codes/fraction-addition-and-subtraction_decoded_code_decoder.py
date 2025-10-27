from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        transformed_expression = expression.replace('-', '+-')
        list_of_fractions = transformed_expression.split('+')
        sum_of_fractions = sum(
            Fraction(frac) for frac in list_of_fractions if frac
        )
        return f"{sum_of_fractions.numerator}/{sum_of_fractions.denominator}"
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        modified_expression = expression.replace('-', '+-')
        list_of_fractions = modified_expression.split('+')
        list_of_valid_fractions = [f for f in list_of_fractions if f]
        result_fraction = sum((Fraction(f) for f in list_of_valid_fractions), start=Fraction(0, 1))
        return f"{result_fraction.numerator}/{result_fraction.denominator}"
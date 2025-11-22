from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # split expression into fractions by replacing '-' with '+-' (except leading '-')
        fractions = expression.replace('-', '+-').split('+')
        # Filter out empty strings and convert to Fraction objects, then sum
        result_fraction = sum(Fraction(frac) for frac in fractions if frac)
        return f"{result_fraction.numerator}/{result_fraction.denominator}"
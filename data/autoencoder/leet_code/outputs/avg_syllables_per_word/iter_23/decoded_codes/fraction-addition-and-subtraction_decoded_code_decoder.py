from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Replace every minus with '+-' to split easily on '+'
        fractions = expression.replace('-', '+-').split('+')
        # Filter out empty strings and convert each fraction string to Fraction
        result = sum(Fraction(frac) for frac in fractions if frac)
        return f"{result.numerator}/{result.denominator}"
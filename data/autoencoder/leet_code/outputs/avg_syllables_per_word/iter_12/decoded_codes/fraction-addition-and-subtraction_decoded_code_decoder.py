from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Insert '+' before any '-' not at start to split fractions properly
        fractions = expression.replace('-', '+-').split('+')
        # Filter out empty strings and convert to Fraction, then sum all
        result = sum(Fraction(frac) for frac in fractions if frac)
        return f"{result.numerator}/{result.denominator}"
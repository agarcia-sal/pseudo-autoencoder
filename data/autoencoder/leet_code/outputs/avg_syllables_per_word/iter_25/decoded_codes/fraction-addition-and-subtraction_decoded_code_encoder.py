from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Insert '+' before each '-' to split easily, then split by '+'
        fractions = [frac for frac in expression.replace('-', '+-').split('+') if frac]
        result = sum(Fraction(frac) for frac in fractions)
        return f"{result.numerator}/{result.denominator}"
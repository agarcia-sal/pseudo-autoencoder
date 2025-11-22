from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = expression.replace('-', '+-').split('+')
        result = sum(Fraction(frac) for frac in fractions if frac)
        return f"{result.numerator}/{result.denominator}"
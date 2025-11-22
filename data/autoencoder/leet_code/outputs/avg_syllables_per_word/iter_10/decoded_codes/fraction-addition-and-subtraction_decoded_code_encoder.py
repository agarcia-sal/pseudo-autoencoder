from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = expression.replace('-', '+-').split('+')
        result = Fraction(0, 1)
        for frac in fractions:
            if frac:
                result += Fraction(frac)
        return f"{result.numerator}/{result.denominator}"
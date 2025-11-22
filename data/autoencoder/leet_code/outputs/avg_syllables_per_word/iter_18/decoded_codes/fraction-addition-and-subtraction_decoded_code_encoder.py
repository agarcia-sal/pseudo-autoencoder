from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Replace every '-' with '+-' to split all fractions by '+'
        fractions = [f for f in expression.replace('-', '+-').split('+') if f]
        # Sum all fractions after converting each to Fraction
        result = sum(Fraction(f) for f in fractions)
        return f"{result.numerator}/{result.denominator}"
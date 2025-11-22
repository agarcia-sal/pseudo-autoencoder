from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Insert '+' before each '-' to split on '+', thus separating all fractions
        fractions = expression.replace('-', '+-').split('+')
        # Sum all non-empty fractions converted to Fraction objects
        result = sum(Fraction(f) for f in fractions if f)
        return f"{result.numerator}/{result.denominator}"
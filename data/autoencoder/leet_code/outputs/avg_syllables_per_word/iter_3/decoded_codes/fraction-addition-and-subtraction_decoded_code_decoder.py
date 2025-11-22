from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        modified_expression = expression.replace('-', '+-')
        fractions = modified_expression.split('+')
        result = sum(Fraction(f) for f in fractions if f)
        return f"{result.numerator}/{result.denominator}"
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        modified_expression = expression.replace('-', '+-')
        fractions_list = modified_expression.split('+')
        filtered_fractions = [f for f in fractions_list if f]
        result = sum(Fraction(frac) for frac in filtered_fractions)
        return f"{result.numerator}/{result.denominator}"